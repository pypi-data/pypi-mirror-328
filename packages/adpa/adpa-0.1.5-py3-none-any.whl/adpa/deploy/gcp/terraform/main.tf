terraform {
  required_version = ">= 1.0.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC Network
resource "google_compute_network" "vpc" {
  name                    = "adpa-${var.environment}-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "adpa-${var.environment}-subnet"
  ip_cidr_range = "10.0.0.0/24"
  network       = google_compute_network.vpc.id
  region        = var.region

  private_ip_google_access = true
}

# Cloud SQL
resource "google_sql_database_instance" "postgres" {
  name             = "adpa-${var.environment}-db"
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = var.database_tier
    
    backup_configuration {
      enabled = true
      start_time = "02:00"
    }
    
    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.vpc.id
    }
    
    insights_config {
      query_insights_enabled = true
      query_string_length    = 1024
      record_application_tags = true
      record_client_address  = true
    }
  }

  deletion_protection = true
}

resource "google_sql_database" "database" {
  name     = "adpa"
  instance = google_sql_database_instance.postgres.name
}

# Cloud Storage
resource "google_storage_bucket" "storage" {
  name          = "adpa-${var.environment}-${var.project_id}"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true
  
  versioning {
    enabled = true
  }

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }
}

# Cloud Functions
resource "google_storage_bucket" "function_source" {
  name          = "adpa-${var.environment}-functions"
  location      = var.region
  force_destroy = true
}

resource "google_cloudfunctions_function" "api" {
  name        = "adpa-${var.environment}-api"
  description = "ADPA Framework API"
  runtime     = "python311"

  available_memory_mb   = var.function_memory
  source_archive_bucket = google_storage_bucket.function_source.name
  source_archive_object = "function-source.zip"
  timeout              = var.function_timeout
  entry_point          = "main"

  environment_variables = {
    ENVIRONMENT = var.environment
  }

  secret_environment_variables {
    key     = "DATABASE_URL"
    secret  = google_secret_manager_secret.database_url.secret_id
    version = "latest"
  }

  vpc_connector = google_vpc_access_connector.connector.id
}

# VPC Access Connector
resource "google_vpc_access_connector" "connector" {
  name          = "adpa-${var.environment}-vpc-connector"
  ip_cidr_range = "10.8.0.0/28"
  network       = google_compute_network.vpc.name
}

# Secret Manager
resource "google_secret_manager_secret" "database_url" {
  secret_id = "adpa-${var.environment}-database-url"
  
  replication {
    automatic = true
  }
}

# Cloud Monitoring
resource "google_monitoring_dashboard" "dashboard" {
  dashboard_json = jsonencode({
    displayName = "ADPA Framework Dashboard"
    gridLayout = {
      widgets = [
        {
          title = "Function Executions"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"cloudfunctions.googleapis.com/function/execution_count\""
                }
              }
            }]
          }
        }
      ]
    }
  })
}

# IAM
resource "google_project_iam_custom_role" "function_role" {
  role_id     = "adpa_function_role"
  title       = "ADPA Function Role"
  description = "Custom role for ADPA Framework functions"
  permissions = [
    "secretmanager.secrets.get",
    "secretmanager.versions.get",
    "cloudsql.instances.connect",
    "storage.objects.get",
    "storage.objects.list"
  ]
}

# Outputs
output "database_connection" {
  value = google_sql_database_instance.postgres.connection_name
  sensitive = true
}

output "function_url" {
  value = google_cloudfunctions_function.api.https_trigger_url
}

output "storage_bucket" {
  value = google_storage_bucket.storage.url
}

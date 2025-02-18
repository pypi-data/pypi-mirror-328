output "vpc_name" {
  description = "The name of the VPC"
  value       = google_compute_network.vpc.name
}

output "subnet_name" {
  description = "The name of the subnet"
  value       = google_compute_subnetwork.subnet.name
}

output "database_name" {
  description = "The name of the Cloud SQL instance"
  value       = google_sql_database_instance.postgres.name
}

output "database_version" {
  description = "The database version"
  value       = google_sql_database_instance.postgres.database_version
}

output "storage_bucket_name" {
  description = "The name of the main storage bucket"
  value       = google_storage_bucket.storage.name
}

output "function_name" {
  description = "The name of the Cloud Function"
  value       = google_cloudfunctions_function.api.name
}

output "function_region" {
  description = "The region of the Cloud Function"
  value       = google_cloudfunctions_function.api.region
}

output "function_service_account" {
  description = "The service account used by the Cloud Function"
  value       = google_cloudfunctions_function.api.service_account_email
}

output "vpc_connector_name" {
  description = "The name of the VPC connector"
  value       = google_vpc_access_connector.connector.name
}

output "monitoring_dashboard_name" {
  description = "The name of the Cloud Monitoring dashboard"
  value       = google_monitoring_dashboard.dashboard.dashboard_json
}

output "custom_role_id" {
  description = "The ID of the custom IAM role"
  value       = google_project_iam_custom_role.function_role.role_id
}

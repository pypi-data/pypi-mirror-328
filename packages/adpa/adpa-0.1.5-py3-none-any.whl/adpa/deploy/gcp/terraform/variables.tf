variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region for resources"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Deployment environment (development, staging, production)"
  type        = string
  default     = "production"

  validation {
    condition     = contains(["development", "staging", "production"], var.environment)
    error_message = "Environment must be one of: development, staging, production."
  }
}

variable "database_tier" {
  description = "Cloud SQL machine type"
  type        = string
  default     = "db-custom-2-4096"
}

variable "database_size_gb" {
  description = "Cloud SQL storage size in GB"
  type        = number
  default     = 20

  validation {
    condition     = var.database_size_gb >= 10
    error_message = "Database size must be at least 10GB."
  }
}

variable "function_memory" {
  description = "Cloud Function memory in MB"
  type        = number
  default     = 1024

  validation {
    condition     = contains([128, 256, 512, 1024, 2048, 4096], var.function_memory)
    error_message = "Function memory must be one of: 128, 256, 512, 1024, 2048, 4096."
  }
}

variable "function_timeout" {
  description = "Cloud Function timeout in seconds"
  type        = number
  default     = 30

  validation {
    condition     = var.function_timeout >= 1 && var.function_timeout <= 540
    error_message = "Function timeout must be between 1 and 540 seconds."
  }
}

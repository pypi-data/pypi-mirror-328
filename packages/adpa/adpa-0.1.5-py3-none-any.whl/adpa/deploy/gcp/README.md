# GCP Deployment

This directory contains Terraform configurations for deploying the ADPA Framework on Google Cloud Platform.

## Prerequisites

1. Terraform installed
2. GCP CLI (gcloud) installed and configured
3. GCP project with required APIs enabled
4. Service account with necessary permissions

## Resources Created

- Cloud Functions for serverless compute
- Cloud Run for containerized services
- Cloud SQL for PostgreSQL database
- Cloud Storage buckets
- Secret Manager for secrets
- Cloud Monitoring
- VPC network components
- IAM roles and permissions

## Deployment Steps

1. Configure GCP credentials:
```bash
gcloud auth application-default login
export GOOGLE_PROJECT=your-project-id
```

2. Update configuration:
```bash
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your settings
```

3. Initialize Terraform:
```bash
terraform init
```

4. Plan deployment:
```bash
terraform plan
```

5. Apply changes:
```bash
terraform apply
```

## Configuration Options

See `terraform.tfvars.example` for available variables:

```hcl
project_id         = "your-project-id"
region            = "us-central1"
environment       = "production"
database_tier     = "db-custom-2-4096"
database_size_gb  = 20
function_memory   = 1024
function_timeout  = 30
```

## Monitoring

1. Cloud Monitoring:
   - Function metrics
   - Database metrics
   - Custom metrics
   - Uptime checks

2. Cloud Logging:
   - Function logs
   - SQL logs
   - Audit logs
   - Error reporting

## Security

1. Network Security:
   - VPC configuration
   - Cloud NAT
   - Firewall rules
   - Private service access

2. Data Security:
   - Customer-managed encryption keys
   - Secret Manager integration
   - IAM roles and permissions
   - VPC Service Controls

## Cost Optimization

1. Resource Management:
   - Right-size instances
   - Autoscaling configuration
   - Storage lifecycle policies
   - Reserved instances

2. Cost Monitoring:
   - Budgets and alerts
   - Cost allocation tags
   - Billing export
   - Resource monitoring

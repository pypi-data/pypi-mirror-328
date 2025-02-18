# AWS Deployment

This directory contains AWS CloudFormation templates and scripts for deploying the ADPA Framework on AWS.

## Prerequisites

1. AWS CLI installed and configured
2. Appropriate IAM permissions
3. AWS account with required service limits

## Resources Created

- API Gateway for REST endpoints
- Lambda functions for serverless compute
- RDS PostgreSQL for database
- S3 buckets for storage
- CloudWatch for monitoring
- Secrets Manager for secrets
- IAM roles and policies
- VPC networking components

## Deployment Steps

1. Configure AWS credentials:
```bash
aws configure
```

2. Update configuration:
```bash
cp config.example.yaml config.yaml
# Edit config.yaml with your settings
```

3. Deploy infrastructure:
```bash
./deploy.sh
```

4. Verify deployment:
```bash
aws cloudformation describe-stacks --stack-name adpa-framework
```

## Configuration Options

See `config.example.yaml` for available configuration options:

```yaml
environment: production
region: us-west-2
vpc:
  cidr: 10.0.0.0/16
  subnets: 3
database:
  instance_class: db.t3.medium
  storage_gb: 20
lambda:
  memory_mb: 1024
  timeout_seconds: 30
```

## Monitoring

1. CloudWatch Metrics:
   - Lambda execution metrics
   - API Gateway metrics
   - RDS metrics
   - Custom application metrics

2. CloudWatch Logs:
   - Lambda function logs
   - API Gateway access logs
   - RDS logs

## Security

1. Network Security:
   - VPC with private subnets
   - Security groups
   - Network ACLs

2. Data Security:
   - Encryption at rest
   - Encryption in transit
   - Secrets management

## Cost Optimization

1. Resource Sizing:
   - Right-size RDS instances
   - Configure Lambda memory
   - Optimize API Gateway usage

2. Cost Monitoring:
   - CloudWatch billing alerts
   - Cost allocation tags
   - Budget monitoring

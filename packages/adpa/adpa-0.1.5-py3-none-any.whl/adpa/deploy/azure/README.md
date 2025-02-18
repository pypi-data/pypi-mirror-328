# Azure Deployment

This directory contains Azure ARM templates and scripts for deploying the ADPA Framework on Azure.

## Prerequisites

1. Azure CLI installed and configured
2. Azure subscription with required permissions
3. Resource providers registered

## Resources Created

- Azure Functions for serverless compute
- Azure API Management for API endpoints
- Azure Database for PostgreSQL
- Azure Storage Account
- Azure Key Vault for secrets
- Application Insights for monitoring
- Virtual Network components
- Managed Identities

## Deployment Steps

1. Configure Azure CLI:
```bash
az login
az account set --subscription <subscription-id>
```

2. Update configuration:
```bash
cp parameters.example.json parameters.json
# Edit parameters.json with your settings
```

3. Deploy infrastructure:
```bash
az deployment group create \
  --name adpa-framework \
  --resource-group adpa-rg \
  --template-file templates/main.json \
  --parameters @parameters.json
```

4. Verify deployment:
```bash
az deployment group show \
  --name adpa-framework \
  --resource-group adpa-rg
```

## Configuration Options

See `parameters.example.json` for available parameters:

```json
{
  "environment": {
    "value": "production"
  },
  "location": {
    "value": "westeurope"
  },
  "databaseTier": {
    "value": "GeneralPurpose"
  },
  "databaseSize": {
    "value": "GP_Gen5_2"
  },
  "functionAppSku": {
    "value": "EP1"
  }
}
```

## Monitoring

1. Application Insights:
   - Function app telemetry
   - API Management metrics
   - Database metrics
   - Custom metrics

2. Log Analytics:
   - Function app logs
   - API Management logs
   - Database logs
   - Platform logs

## Security

1. Network Security:
   - Virtual Network integration
   - Private endpoints
   - Network security groups

2. Data Security:
   - Encryption at rest
   - TLS/SSL configuration
   - Managed identities
   - Key Vault integration

## Cost Optimization

1. Resource Sizing:
   - Right-size database
   - Configure function app scaling
   - Optimize API Management tier

2. Cost Monitoring:
   - Azure Cost Management
   - Budget alerts
   - Resource tagging

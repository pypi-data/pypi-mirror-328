# ADPA Framework Documentation

**Version: 1.4.0**
**Release Date: 2025-02-07**

## Overview

The ADPA (Autonomous Distributed Processing Agents) Framework is a powerful system for managing and orchestrating AI agents across distributed environments. This documentation provides comprehensive information about the framework's components, features, and best practices.

## What's New in 1.4.0

### Security Enhancements
- CSRF Protection ✓
  - Token-based protection
  - Cookie-based storage
  - Configurable settings
- Input Sanitization (Next)
  - XSS prevention
  - SQL injection protection
  - Input validation
- Rate Limiting (Planned)
  - Per-endpoint limits
  - Token bucket algorithm
  - Rate limit headers

### Code Quality
- Type Hints (In Progress)
  - Added to core modules
  - CI type checking
  - Documentation updates
- Pydantic Models
  - Configuration validation
  - Data validation
  - Custom validators

### Monitoring System
- System metrics
  - CPU, memory, GPU usage
  - Disk utilization
  - Network statistics
- Training metrics
  - Loss tracking
  - Validation metrics
  - Model performance
- Alert system
  - Multiple channels (Slack, Email, MLflow)
  - Customizable thresholds
  - Alert management

## Quick Start

1. **Installation**
   ```bash
   pip install adpa-framework
   ```

2. **Basic Configuration**
   ```python
   from adpa import Framework
   
   framework = Framework()
   framework.configure(config_path="config.yaml")
   ```

3. **Launch Management Interface**
   ```bash
   streamlit run examples/streamlit/Home.py
   ```

## Core Components

### 1. Text2SQL Module
- Natural language to SQL conversion
- Query validation and security
- Performance optimization
- Error handling

### 2. Security Module
- CSRF protection
- Input sanitization
- Rate limiting
- Authentication

### 3. Monitoring Module
- System monitoring
- Training metrics
- Alert management
- Performance tracking

### 4. Core Module
- Workflow management
- State handling
- Type system
- Configuration

## Documentation Structure

1. **Getting Started**
   - [Setup Guide](setup_guide.md)
   - [Basic Usage](guides/basic_usage.md)
   - [Configuration](guides/configuration.md)

2. **Components**
   - [Text2SQL](components/text2sql.md)
   - [Security](components/security.md)
   - [Monitoring](components/monitoring.md)
   - [Core](components/core.md)

3. **Development**
   - [Architecture](architecture/overview.md)
   - [Contributing](development/contributing.md)
   - [Testing](testing/overview.md)
   - [Security](security/overview.md)

4. **API Reference**
   - [Core API](api/core.md)
   - [Text2SQL API](api/text2sql.md)
   - [Security API](api/security.md)
   - [Monitoring API](api/monitoring.md)

5. **Examples & Tutorials**
   - [Basic Examples](examples/basic.md)
   - [Advanced Usage](examples/advanced.md)
   - [Integration](examples/integration.md)

6. **Release Information**
   - [Changelog](CHANGELOG.md)
   - [Roadmap](development_roadmap.md)
   - [Migration Guide](guides/migration.md)

## Community & Support

- [GitHub Issues](https://github.com/codeium/adpa/issues)
- [Discord Community](https://discord.gg/codeium)
- [Documentation Updates](https://github.com/codeium/adpa/docs)
- [Contributing Guidelines](CONTRIBUTING.md)

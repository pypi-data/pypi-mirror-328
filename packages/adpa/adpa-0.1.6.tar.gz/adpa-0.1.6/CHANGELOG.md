# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Enhanced testing environment with file-based output capture
- Added troubleshooting documentation for test output issues
- Implemented test quality checks with file-based logging

### Changed
- Updated test_quality.py to use file-based output instead of logging
- Modified test execution approach to handle output capture issues

## [1.5.0] - 2025-02-10

### Added

- Enhanced documentation system:
  - Comprehensive user guides for Agents and Text2SQL
  - Detailed API references
  - Extended examples with code snippets
  - Improved configuration documentation
- Expanded test coverage:
  - API tests for Text2SQL endpoints
  - Performance tests with load testing
  - Enhanced test utilities and keywords
  - Resource monitoring
- Enhanced CI/CD pipeline:
  - Matrix testing for multiple Python versions
  - Performance testing integration
  - Documentation deployment
  - Package publishing
  - Slack notifications
  - PostgreSQL service for integration tests

### Changed

- Updated package configuration in pyproject.toml
- Migrated to Poetry build system
- Enhanced GitHub Actions workflow
- Improved test organization

## [1.4.1] - 2025-02-09

### Added

- Migrated UI components to new `src/adpa/ui` structure
- Enhanced database storage management interface
- Added API integration interface
- Improved error handling and logging
- Added comprehensive type hints
- Enhanced documentation

### Changed

- Reorganized project structure
- Updated gitignore patterns
- Improved code organization
- Enhanced security features

### Removed

- Old `streamlit_app` directory structure

## [1.4.0] - 2025-02-07

### Added

- CSRF Protection
- Security monitoring
- Initial UI components

### Changed

- Enhanced code quality
- Improved documentation
- Updated dependencies

## [1.4.1] - 2025-02-09

### Added

- Enhanced Text2SQL module with:
  - Comprehensive schema validation
  - SQL injection prevention
  - Query optimization suggestions
  - Natural language query parsing
  - Template management
- Expanded Agents module with:
  - Resource monitoring
  - Health checks
  - Retry mechanisms
  - Security configurations
  - Message passing system
- Comprehensive test suite for both modules
- Additional dependencies for enhanced functionality

### Changed

- Updated requirements.txt with new dependencies
- Improved test coverage with pytest-asyncio
- Enhanced documentation

## [1.4.0] - 2025-02-09

### Added

- Text2SQL component with natural language query support
- Agent system for distributed processing
- Real-time monitoring system
- FastAPI-based REST API
- Comprehensive documentation
- GUI with React and Material-UI
- Testing infrastructure with pytest and Robot Framework

### Changed

- Reorganized package structure to src-based layout
- Updated dependency management
- Improved error handling and logging
- Enhanced security features

### Fixed

- Various bug fixes and performance improvements

## [1.3.0] - 2025-01-15

### Added

- Initial release of core functionality
- Basic Text2SQL support
- Simple monitoring
- Basic API endpoints

### Changed

- Improved documentation
- Updated dependencies

### Fixed

- Initial bug fixes

## [1.2.0] - 2024-12-01

### Added

- Prototype implementation
- Basic features and testing

## [1.1.0] - 2024-11-15

### Added

- Initial project setup
- Basic documentation

## [1.0.0] - 2024-11-01

### Added

- Project initialization

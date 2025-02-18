# ADPA Framework Validation System

## Overview

The ADPA Framework Validation System is a comprehensive suite of tools designed to enforce coding standards, best practices, and quality guidelines across the entire codebase. It provides automated checks for Python code, Robot Framework tests, Streamlit applications, and Pydantic models.

## Components

### 1. Code Quality Validator

Enforces general code quality standards:

- File length limits (max 500 lines)
- Function length limits (max 50 lines)
- Class length limits (max 200 lines)
- Line length limits (max 100 characters)
- Cyclomatic complexity (max 10)
- Docstring requirements
- Type hint enforcement

```python
from adpa.validators import CodeQualityChecker

checker = CodeQualityChecker(project_root)
violations = checker.check_project()
```

### 2. Robot Framework Validator

Ensures Robot Framework tests follow best practices:

- Test case naming (`Test Should *`)
- Required tags (smoke, regression, integration)
- Gherkin syntax (Given/When/Then)
- Documentation requirements
- Resource file structure
- Keyword organization

```python
from adpa.validators import RobotValidator

# Validate a test case
test_cases = RobotValidator.parse_test_case(content)
issues = RobotValidator.validate_test_case(test_cases[0])

# Validate a resource file
issues = RobotValidator.validate_resource_file(file_path)
```

### 3. Streamlit Validator

Validates Streamlit applications:

- Page configuration
- Session state management
- Form validation
- Caching implementation
- Error handling
- Performance optimization

```python
from adpa.validators import StreamlitValidator

# Validate a Streamlit page
issues = StreamlitValidator.validate_page(page_path)

# Check performance
performance_issues = StreamlitValidator.check_performance(page_path)
```

### 4. Pydantic Validator

Ensures proper use of Pydantic models:

- Model structure
- Field validation
- Documentation requirements
- Type enforcement
- Configuration settings

```python
from adpa.validators import ModelValidator

# Validate model structure
issues = ModelValidator.validate_model_structure(UserProfile)

# Validate model instance
instance_issues = ModelValidator.validate_model_instance(user)
```

## Configuration

The validation system is highly configurable through YAML configuration files:

```yaml
code_quality:
  max_file_length: 500
  max_function_length: 50
  max_class_length: 200
  max_line_length: 100
  max_complexity: 10
  required_docstring: true
  enforce_type_hints: true

robot:
  required_tags:
    - smoke
    - regression
    - integration
  enforce_gherkin: true
  require_documentation: true

streamlit:
  require_page_config: true
  enforce_session_state_init: true
  enforce_form_validation: true
  require_caching: true

pydantic:
  require_frozen: true
  require_validation: true
  require_descriptions: true
  require_examples: true
```

## Integration

### Pre-commit Hook

The validation system can be integrated into your git workflow:

```bash
#!/bin/sh
python scripts/code_quality_check.py
```

### CI/CD Pipeline

Automated validation in GitHub Actions:

```yaml
- name: Run code quality checks
  run: python scripts/code_quality_check.py

- name: Run tests with coverage
  run: pytest tests/ --cov=adpa
```

## Best Practices

### 1. Code Organization

- Keep files under 500 lines
- Split large functions into smaller ones
- Use clear, descriptive names
- Follow type hinting conventions

### 2. Testing

- Write tests in Gherkin style
- Include all required tags
- Document test cases
- Use page objects for UI tests

### 3. Streamlit Development

- Initialize session state properly
- Use caching for expensive operations
- Implement proper error handling
- Validate form inputs

### 4. Model Development

- Use Pydantic for data validation
- Include field descriptions
- Provide examples
- Implement custom validators

## Troubleshooting

Common issues and solutions:

1. **File Length Violations**
   - Split into multiple files
   - Extract reusable components
   - Create utility modules

2. **Missing Documentation**
   - Add docstrings to all public functions
   - Include parameter descriptions
   - Document return values
   - Add usage examples

3. **Type Hint Issues**
   - Use type hints consistently
   - Import types from typing module
   - Use Union for multiple types
   - Add Generic types where needed

4. **Performance Issues**
   - Implement caching
   - Optimize database queries
   - Use async operations
   - Batch process where possible

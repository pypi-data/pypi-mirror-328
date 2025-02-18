# ADPA Framework Templates

This directory contains templates used throughout the ADPA Framework.

## Directory Structure

```
templates/
├── html/              # HTML templates
│   ├── base.html     # Base template
│   └── components/   # Reusable components
├── markdown/         # Markdown templates
│   ├── docs/        # Documentation templates
│   └── reports/     # Report templates
└── sql/             # SQL templates
    ├── queries/     # Query templates
    └── schema/      # Schema templates
```

## Template Categories

### HTML Templates
- Base templates for web interfaces
- Reusable UI components
- Transcript viewers
- Result displays

### Markdown Templates
- Documentation templates
- Report templates
- Release notes
- Change logs

### SQL Templates
- Query templates
- Schema definitions
- Migration templates
- Test data templates

## Usage Guidelines

### 1. Template Variables
- Use descriptive names
- Document all variables
- Provide default values
- Use type hints

### 2. Template Inheritance
- Use base templates
- Create reusable blocks
- Keep DRY principle
- Document extensions

### 3. Styling
- Use consistent formatting
- Follow style guide
- Include comments
- Document dependencies

### 4. Security
- Escape user input
- Validate variables
- Use safe filters
- Prevent XSS

## Contributing

1. Follow naming conventions
2. Add documentation
3. Include examples
4. Test templates
5. Update README

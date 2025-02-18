# Contributing to ADPA

First off, thank you for considering contributing to ADPA! It's people like you that make ADPA such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Pull Request Process

1. Update the README.md with details of changes to the interface
2. Update the CHANGELOG.md with a note describing your changes
3. The PR will be merged once you have the sign-off of two other developers

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/adpa.git
   cd adpa
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install poetry
   poetry install --with dev,test,docs
   ```

4. Install pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

## Code Style

We follow strict coding standards to maintain high code quality and consistency:

### Python Style Guide

1. Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
2. Use [Google style](https://google.github.io/styleguide/pyguide.html) docstrings
3. Maximum line length: 100 characters
4. Use type hints for all functions and variables
5. Sort imports using isort
6. Use double quotes for strings

### Code Organization

1. Maximum file length: 500 lines
2. Maximum function length: 50 lines
3. Maximum class length: 200 lines
4. Maximum cyclomatic complexity: 10

### Naming Conventions

1. Classes: PascalCase (e.g., `UserManager`)
2. Functions: snake_case (e.g., `process_data`)
3. Variables: snake_case (e.g., `user_count`)
4. Constants: SCREAMING_SNAKE_CASE (e.g., `MAX_RETRIES`)
5. Private members: _prefix (e.g., `_internal_state`)

## Testing

### Unit Tests

1. Use pytest for unit testing
2. Maintain minimum 80% code coverage
3. Test both success and error cases
4. Mock external dependencies
5. Keep tests focused and concise

### Robot Framework Tests

1. Follow BDD style with Given/When/Then
2. Organize tests by feature
3. Use descriptive test names
4. Include proper documentation
5. Add appropriate tags

## Documentation

1. Keep documentation up to date
2. Include code examples
3. Document all public APIs
4. Add type hints and docstrings
5. Update CHANGELOG.md

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation only
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding or updating tests
- chore: Maintenance tasks

## Branch Naming

- Feature branches: `feature/description`
- Bug fixes: `fix/description`
- Documentation: `docs/description`
- Release branches: `release/version`

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create a release branch
4. Create and push a tag
5. CI/CD will handle the release

## Getting Help

1. Check the [documentation](https://adpa.readthedocs.io)
2. Ask in [GitHub Discussions](https://github.com/achimdehnert/adpa/discussions)
3. Open an [issue](https://github.com/achimdehnert/adpa/issues)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

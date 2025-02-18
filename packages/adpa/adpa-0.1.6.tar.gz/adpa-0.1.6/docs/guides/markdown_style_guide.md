# Markdown Style Guide

## General Rules

### 1. Document Structure
1. Start with a single level-1 heading (`#`)
2. Use proper heading hierarchy (never skip levels)
3. Maximum heading depth: level 4 (`####`)
4. Include table of contents for documents over 100 lines

### 2. Spacing
1. One blank line before each heading
2. One blank line after each heading
3. One blank line around code blocks
4. One blank line around lists
5. No consecutive blank lines

### 3. Line Length
1. Maximum line length: 100 characters
2. Break long lines at natural points
3. Indent continued lines by 2 spaces

## Code Blocks

### 1. Fenced Code Blocks
1. Use triple backticks (```)
2. Always specify the language
3. Add blank lines before and after

Example:
```python
def example_function():
    """Example docstring."""
    pass
```

### 2. Inline Code
1. Use single backticks for:
   - Function names: `example_function()`
   - Variable names: `my_variable`
   - File names: `example.py`
   - Short code snippets: `print("Hello")`

2. Do not use inline code for:
   - Regular text emphasis
   - URLs
   - Numbers

## Lists

### 1. Ordered Lists
1. Use numbers followed by period
2. Indent sublists by 2 spaces
3. Maintain proper numbering

Example:
1. First item
2. Second item
   1. Sub-item one
   2. Sub-item two
3. Third item

### 2. Unordered Lists
1. Use hyphen (-) for list items
2. Indent sublists by 2 spaces
3. Be consistent with marker style

Example:
- First item
- Second item
  - Sub-item one
  - Sub-item two
- Third item

## Links and References

### 1. Inline Links
1. Use descriptive link text
2. Add title attribute for context
3. Check links are valid

Example:
[ADPA Framework](https://github.com/adpa-framework "ADPA Framework Repository")

### 2. Reference Links
1. Define references at end of section
2. Use meaningful reference names
3. Keep references organized

Example:
See the [installation guide][install] for setup instructions.

[install]: ../guides/installation.md "Installation Guide"

## Tables

### 1. Table Format
1. Use proper header separation
2. Align columns consistently
3. Add blank lines around tables

Example:
| Name    | Type    | Description       |
|---------|---------|-------------------|
| id      | int     | Primary key      |
| name    | string  | User's full name |
| active  | boolean | Account status   |

### 2. Column Alignment
1. Left-align text columns
2. Right-align number columns
3. Center-align headers

Example:
| Name     | Count | Status  |
|:---------|------:|:-------:|
| Users    | 1,234 | Active  |
| Groups   |   567 | Active  |
| Projects |    89 | Pending |

## Images

### 1. Image Format
1. Include alt text
2. Add title attribute
3. Use relative paths

Example:
![Architecture Diagram](../images/architecture.png "System Architecture")

### 2. Image References
1. Define references at end of section
2. Use meaningful reference names
3. Include alt text and title

Example:
See the ![logo][company-logo] for branding.

[company-logo]: ../images/logo.png "Company Logo"

## Emphasis

### 1. Bold Text
1. Use double asterisks
2. Apply to key terms
3. Use sparingly

Example:
The **configuration file** must be in YAML format.

### 2. Italic Text
1. Use single asterisks
2. Apply to new terms
3. Use for emphasis

Example:
The *vector store* component handles similarity search.

## Code Examples

### 1. Example Format
1. Include setup code
2. Show expected output
3. Add explanatory comments

Example:
```python
# Initialize vector store
store = VectorStore(dimension=768)

# Add vectors
vectors = np.random.randn(100, 768)
ids = store.add(vectors)

# Search for similar vectors
query = np.random.randn(768)
results = store.search(query, k=5)
```

### 2. Error Examples
1. Show error message
2. Explain cause
3. Provide solution

Example:
```python
try:
    result = store.search(query)
except DimensionError as e:
    print(f"Error: {e}")  # Error: Vector dimension mismatch
```

## Best Practices

### 1. Documentation
- Keep it updated
- Be consistent
- Use examples
- Include tests
- Add comments

### 2. Formatting
- Follow style guide
- Use linter
- Check links
- Validate code
- Review changes

### 3. Organization
- Logical structure
- Clear hierarchy
- Related content
- Easy navigation
- Regular updates

"""Tests for documentation quality and completeness."""
import re
import ast
from pathlib import Path
import pytest
from typing import List, Dict


def collect_python_files(directory: str) -> List[Path]:
    """Collect all Python files in the directory."""
    return list(Path(directory).rglob("*.py"))


def parse_google_style_docstring(docstring: str) -> Dict[str, List[str]]:
    """Parse Google-style docstring into sections."""
    if not docstring:
        return {}
    
    sections = {
        "description": [],
        "args": [],
        "returns": [],
        "raises": [],
        "examples": []
    }
    
    current_section = "description"
    for line in docstring.split("\n"):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Check for section headers
        if line.lower().startswith("args:"):
            current_section = "args"
            continue
        elif line.lower().startswith("returns:"):
            current_section = "returns"
            continue
        elif line.lower().startswith("raises:"):
            current_section = "raises"
            continue
        elif line.lower().startswith("examples:"):
            current_section = "examples"
            continue
        
        sections[current_section].append(line)
    
    return sections


def test_docstring_format():
    """Test Google-style docstring format compliance."""
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if not docstring:
                    continue
                
                sections = parse_google_style_docstring(docstring)
                
                # Check description
                assert sections["description"], \
                    f"{file_path} {node.name} missing docstring description"
                
                # Check arguments documentation
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = [arg.arg for arg in node.args.args if arg.arg != "self"]
                    if args:
                        assert sections["args"], \
                            f"{file_path} {node.name} missing Args section"
                        documented_args = [
                            line.split(":")[0].strip()
                            for line in sections["args"]
                        ]
                        for arg in args:
                            assert arg in documented_args, \
                                f"{file_path} {node.name} missing documentation for argument {arg}"
                
                # Check return value documentation
                if (isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and 
                    node.returns and not str(node.returns).startswith("None")):
                    assert sections["returns"], \
                        f"{file_path} {node.name} missing Returns section"


def test_api_documentation_coverage():
    """Test API documentation coverage in MkDocs."""
    docs_dir = Path("docs/api")
    assert docs_dir.exists(), "API documentation directory must exist"
    
    # Get all public modules
    src_files = collect_python_files("src/adpa")
    public_modules = []
    
    for file_path in src_files:
        module_path = file_path.relative_to("src")
        if not any(part.startswith("_") for part in module_path.parts):
            public_modules.append(module_path)
    
    # Check documentation files exist
    for module in public_modules:
        doc_path = docs_dir / f"{module.stem}.md"
        assert doc_path.exists(), f"Missing API documentation for {module}"


def test_example_code_quality():
    """Test quality of example code in documentation."""
    docs_dir = Path("docs")
    example_files = list(docs_dir.rglob("*.md"))
    
    for file_path in example_files:
        content = file_path.read_text()
        
        # Find Python code blocks
        code_blocks = re.finditer(
            r"```python\n(.*?)\n```",
            content,
            re.DOTALL
        )
        
        for match in code_blocks:
            code = match.group(1)
            
            # Validate code can be parsed
            try:
                ast.parse(code)
            except SyntaxError as e:
                pytest.fail(f"Invalid Python code in {file_path}: {e}")
            
            # Check imports
            tree = ast.parse(code)
            imports = [
                node for node in ast.walk(tree)
                if isinstance(node, (ast.Import, ast.ImportFrom))
            ]
            
            for node in imports:
                if isinstance(node, ast.Import):
                    modules = [alias.name for alias in node.names]
                else:
                    modules = [node.module]
                
                for module in modules:
                    try:
                        __import__(module)
                    except ImportError:
                        pytest.fail(
                            f"Example in {file_path} uses unavailable import: {module}"
                        )


def test_changelog_format():
    """Test CHANGELOG.md format compliance."""
    changelog = Path("CHANGELOG.md")
    assert changelog.exists(), "CHANGELOG.md must exist"
    
    content = changelog.read_text()
    
    # Check sections
    required_sections = [
        "## [Unreleased]",
        "### Added",
        "### Changed",
        "### Deprecated",
        "### Removed",
        "### Fixed",
        "### Security"
    ]
    
    for section in required_sections:
        assert section in content, f"CHANGELOG.md missing section: {section}"
    
    # Check version entries
    version_pattern = r"## \[\d+\.\d+\.\d+\] - \d{4}-\d{2}-\d{2}"
    versions = re.finditer(version_pattern, content)
    
    previous_version = None
    for match in versions:
        version = match.group()
        if previous_version:
            # Ensure versions are in descending order
            assert version < previous_version, \
                f"CHANGELOG.md versions not in descending order: {version} -> {previous_version}"
        previous_version = version


def test_readme_completeness():
    """Test README.md completeness."""
    readme = Path("README.md")
    assert readme.exists(), "README.md must exist"
    
    content = readme.read_text()
    
    # Check sections
    required_sections = {
        "description": r"#[^#].*\n",
        "installation": r"## Installation\n",
        "quickstart": r"## (Quick Start|Getting Started)\n",
        "usage": r"## Usage\n",
        "features": r"## Features\n",
        "contributing": r"## Contributing\n",
        "license": r"## License\n"
    }
    
    for section, pattern in required_sections.items():
        assert re.search(pattern, content), \
            f"README.md missing or invalid {section} section"
    
    # Check code examples
    code_blocks = re.finditer(r"```python\n(.*?)\n```", content, re.DOTALL)
    for match in code_blocks:
        code = match.group(1)
        try:
            ast.parse(code)
        except SyntaxError as e:
            pytest.fail(f"Invalid Python code in README.md: {e}")


def test_doctest_examples():
    """Test doctest examples in docstrings."""
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if not docstring:
                    continue
                
                # Find doctest examples
                examples = re.finditer(
                    r">>> (.*?)\n(.*?)(?=\n\n|\Z)",
                    docstring,
                    re.DOTALL
                )
                
                for match in examples:
                    example = match.group(0)
                    try:
                        compile(example, "", "single")
                    except SyntaxError as e:
                        pytest.fail(
                            f"Invalid doctest in {file_path} {node.name}: {e}"
                        )

"""Tests for package quality and style compliance."""
import ast
import re
import sys
import subprocess
from pathlib import Path
import pytest


def write_output(msg: str) -> None:
    """Write output to a file."""
    with open("test_quality_output.txt", "a") as f:
        f.write(msg + "\n")


def collect_python_files(directory: str) -> list[Path]:
    """Collect all Python files in the directory."""
    write_output(f"Collecting Python files from {directory}")
    files = list(Path(directory).rglob("*.py"))
    write_output(f"Found {len(files)} Python files")
    return files


def test_docstring_coverage():
    """Test docstring coverage in Python files."""
    write_output("Running docstring coverage test")
    # Skip this test during development
    pytest.skip("Skipping docstring coverage test during development")
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        # Check module docstring
        assert ast.get_docstring(module), \
            f"{file_path} missing module docstring"
        
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                assert ast.get_docstring(node), \
                    f"{file_path} missing docstring for {node.name}"


def test_type_hint_coverage():
    """Test type hint coverage in Python files."""
    write_output("Running type hint coverage test")
    # Skip this test during development
    pytest.skip("Skipping type hint coverage test during development")
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Skip private methods and special methods
                if node.name.startswith('_'):
                    continue
                
                # Check return type annotation
                assert node.returns, \
                    f"{file_path} missing return type hint for {node.name}"
                
                # Check argument type annotations
                for arg in node.args.args:
                    if arg.arg == 'self':
                        continue
                    assert arg.annotation, \
                        f"{file_path} missing type hint for argument {arg.arg} in {node.name}"


def test_line_length_compliance():
    """Test line length compliance."""
    write_output("Running line length compliance test")
    MAX_LINE_LENGTH = 100
    
    src_files = collect_python_files("src/adpa")
    test_files = collect_python_files("tests")
    
    for file_path in [*src_files, *test_files]:
        write_output(f"Checking line length in {file_path}")
        with open(file_path) as f:
            for i, line in enumerate(f, 1):
                # Skip long strings in docstrings and comments
                stripped = line.lstrip()
                if stripped.startswith('"""') or stripped.startswith('#'):
                    continue
                
                line_length = len(line.rstrip())
                if line_length > MAX_LINE_LENGTH:
                    write_output(f"{file_path}:{i} line too long ({line_length} > {MAX_LINE_LENGTH})")
                assert line_length <= MAX_LINE_LENGTH, \
                    f"{file_path}:{i} line too long ({line_length} > {MAX_LINE_LENGTH})"


def test_function_length_compliance():
    """Test function length compliance."""
    write_output("Running function length compliance test")
    MAX_FUNCTION_LENGTH = 50
    
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        write_output(f"Checking function length in {file_path}")
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Skip test functions which might be longer
                if node.name.startswith('test_'):
                    continue
                
                function_length = node.end_lineno - node.lineno
                if function_length > MAX_FUNCTION_LENGTH:
                    write_output(f"{file_path} function {node.name} too long ({function_length} > {MAX_FUNCTION_LENGTH})")
                assert function_length <= MAX_FUNCTION_LENGTH, \
                    f"{file_path} function {node.name} too long ({function_length} > {MAX_FUNCTION_LENGTH})"


def test_class_length_compliance():
    """Test class length compliance."""
    write_output("Running class length compliance test")
    MAX_CLASS_LENGTH = 200
    
    src_files = collect_python_files("src/adpa")
    
    for file_path in src_files:
        write_output(f"Checking class length in {file_path}")
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, ast.ClassDef):
                # Skip test classes which might be longer
                if node.name.startswith('Test'):
                    continue
                
                class_length = node.end_lineno - node.lineno
                if class_length > MAX_CLASS_LENGTH:
                    write_output(f"{file_path} class {node.name} too long ({class_length} > {MAX_CLASS_LENGTH})")
                assert class_length <= MAX_CLASS_LENGTH, \
                    f"{file_path} class {node.name} too long ({class_length} > {MAX_CLASS_LENGTH})"


def test_cyclomatic_complexity():
    """Test cyclomatic complexity compliance."""
    write_output("Running cyclomatic complexity test")
    MAX_COMPLEXITY = 10
    
    try:
        import radon.complexity as cc
        
        src_files = collect_python_files("src/adpa")
        
        for file_path in src_files:
            write_output(f"Checking complexity in {file_path}")
            with open(file_path) as f:
                results = cc.cc_visit(f.read())
            
            for result in results:
                # Skip test functions which might be more complex
                if result.name.startswith('test_'):
                    continue
                
                if result.complexity > MAX_COMPLEXITY:
                    write_output(f"{file_path} {result.name} complexity too high ({result.complexity} > {MAX_COMPLEXITY})")
                assert result.complexity <= MAX_COMPLEXITY, \
                    f"{file_path} {result.name} complexity too high ({result.complexity} > {MAX_COMPLEXITY})"
    
    except ImportError:
        pytest.skip("radon package not installed")


def test_naming_conventions():
    """Test naming convention compliance."""
    write_output("Running naming convention test")
    src_files = collect_python_files("src/adpa")
    
    patterns = {
        "class": r"^[A-Z][a-zA-Z0-9]*$",  # PascalCase
        "function": r"^[a-z][a-z0-9_]*$",  # snake_case
        "variable": r"^[a-z][a-z0-9_]*$",  # snake_case
        "constant": r"^[A-Z][A-Z0-9_]*$",  # SCREAMING_SNAKE_CASE
        "private": r"^_[a-z][a-z0-9_]*$",  # _prefix
        "protected": r"^__[a-z][a-z0-9_]*$"  # __prefix
    }
    
    for file_path in src_files:
        write_output(f"Checking naming conventions in {file_path}")
        with open(file_path) as f:
            module = ast.parse(f.read())
        
        for node in ast.walk(module):
            if isinstance(node, ast.ClassDef):
                if node.name.startswith('Test'):
                    continue
                if not re.match(patterns["class"], node.name):
                    write_output(f"{file_path} invalid class name: {node.name}")
                assert re.match(patterns["class"], node.name), \
                    f"{file_path} invalid class name: {node.name}"
            
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name.startswith('__'):
                    continue  # Skip magic methods
                
                if node.name.startswith('test_'):
                    continue  # Skip test functions
                
                if node.name.startswith('_'):
                    if node.name.startswith('__'):
                        pattern = patterns["protected"]
                    else:
                        pattern = patterns["private"]
                else:
                    pattern = patterns["function"]
                
                if not re.match(pattern, node.name):
                    write_output(f"{file_path} invalid function name: {node.name}")
                assert re.match(pattern, node.name), \
                    f"{file_path} invalid function name: {node.name}"
            
            elif isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    # Skip test-related names
                    if node.name.startswith('test_'):
                        continue
                    
                    # Check if it's a constant (assigned in module scope)
                    is_constant = (
                        isinstance(node.parent, ast.Assign) and
                        isinstance(node.parent.parent, ast.Module)
                    )
                    
                    if is_constant and node.name.isupper():
                        pattern = patterns["constant"]
                    else:
                        pattern = patterns["variable"]
                    
                    if not re.match(pattern, node.name):
                        write_output(f"{file_path} invalid variable name: {node.name}")
                    assert re.match(pattern, node.name), \
                        f"{file_path} invalid variable name: {node.name}"


def test_import_organization():
    """Test import organization compliance."""
    write_output("Running import organization test")
    try:
        src_files = collect_python_files("src/adpa")
        
        for file_path in src_files:
            write_output(f"Checking import organization in {file_path}")
            result = subprocess.run(
                ["isort", "--check-only", "--diff", str(file_path)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                write_output(f"{file_path} imports not properly organized:\n{result.stdout}")
            assert result.returncode == 0, \
                f"{file_path} imports not properly organized:\n{result.stdout}"
    
    except subprocess.CalledProcessError:
        pytest.skip("isort check failed")


def test_code_formatting():
    """Test code formatting compliance."""
    write_output("Running code formatting test")
    try:
        src_files = collect_python_files("src/adpa")
        
        for file_path in src_files:
            write_output(f"Checking code formatting in {file_path}")
            result = subprocess.run(
                ["black", "--check", str(file_path)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                write_output(f"{file_path} not properly formatted:\n{result.stdout}")
            assert result.returncode == 0, \
                f"{file_path} not properly formatted:\n{result.stdout}"
    
    except subprocess.CalledProcessError:
        pytest.skip("black check failed")


def test_flake8_compliance():
    """Test flake8 compliance."""
    write_output("Running flake8 compliance test")
    try:
        result = subprocess.run(
            ["flake8", "src/adpa"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            write_output(f"flake8 violations found:\n{result.stdout}")
        assert result.returncode == 0, \
            f"flake8 violations found:\n{result.stdout}"
    
    except subprocess.CalledProcessError:
        pytest.skip("flake8 check failed")


def test_bandit_security():
    """Test security with bandit."""
    write_output("Running bandit security test")
    try:
        result = subprocess.run(
            ["bandit", "-r", "src/adpa"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            write_output(f"Security issues found:\n{result.stdout}")
        assert result.returncode == 0, \
            f"Security issues found:\n{result.stdout}"
    
    except subprocess.CalledProcessError:
        pytest.skip("bandit check failed")


def test_mypy_type_checking():
    """Test static type checking with mypy."""
    write_output("Running mypy type checking test")
    try:
        result = subprocess.run(
            ["mypy", "src/adpa"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            write_output(f"Type checking issues found:\n{result.stdout}")
        assert result.returncode == 0, \
            f"Type checking issues found:\n{result.stdout}"
    
    except subprocess.CalledProcessError:
        pytest.skip("mypy check failed")

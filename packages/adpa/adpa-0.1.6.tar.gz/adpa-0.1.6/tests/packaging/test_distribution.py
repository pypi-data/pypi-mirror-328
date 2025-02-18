"""Tests for package distribution and PyPI compatibility."""
import os
import re
import json
import subprocess
from pathlib import Path
import pytest
from packaging import version


def test_package_classifiers():
    """Test PyPI classifiers in package metadata."""
    pyproject_path = Path("pyproject.toml")
    assert pyproject_path.exists()
    
    with open(pyproject_path) as f:
        import toml
        pyproject = toml.load(f)
    
    classifiers = pyproject["tool"]["poetry"]["classifiers"]
    required_categories = [
        "Development Status",
        "Intended Audience",
        "License",
        "Programming Language :: Python",
        "Operating System",
        "Topic"
    ]
    
    # Check presence of required classifier categories
    classifier_categories = [c.split(" :: ")[0] for c in classifiers]
    for required in required_categories:
        assert any(required in category for category in classifier_categories), \
            f"Missing classifier category: {required}"


def test_package_urls():
    """Test package URLs in metadata."""
    pyproject_path = Path("pyproject.toml")
    with open(pyproject_path) as f:
        import toml
        pyproject = toml.load(f)
    
    urls = pyproject["tool"]["poetry"]["urls"]
    required_urls = {
        "Homepage": "https://github.com/achimdehnert/adpa",
        "Documentation": "https://adpa.readthedocs.io",
        "Repository": "https://github.com/achimdehnert/adpa.git",
        "Issues": "https://github.com/achimdehnert/adpa/issues",
        "Changelog": "https://github.com/achimdehnert/adpa/blob/main/CHANGELOG.md"
    }
    
    for key, url in required_urls.items():
        assert urls.get(key) == url, f"Missing or incorrect {key} URL"


def test_readme_rendering():
    """Test README.md rendering compatibility with PyPI."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md must exist"
    
    # Check README content
    content = readme_path.read_text()
    
    # Check for required sections
    required_sections = [
        "# ADPA",
        "## Installation",
        "## Features",
        "## Documentation",
        "## Contributing",
        "## License"
    ]
    for section in required_sections:
        assert section in content, f"README missing section: {section}"
    
    # Check for badges
    badge_patterns = [
        r"!\[PyPI version\]",
        r"!\[Python\]",
        r"!\[License\]",
        r"!\[Documentation Status\]"
    ]
    for pattern in badge_patterns:
        assert re.search(pattern, content), f"README missing badge: {pattern}"


def test_manifest_completeness():
    """Test MANIFEST.in completeness."""
    manifest_path = Path("MANIFEST.in")
    assert manifest_path.exists(), "MANIFEST.in must exist"
    
    content = manifest_path.read_text()
    required_patterns = [
        "include LICENSE",
        "include README.md",
        "include CHANGELOG.md",
        "include pyproject.toml",
        "include VERSION",
        "recursive-include src *",
        "recursive-include tests *",
        "recursive-include docs *",
        "global-exclude *.py[cod]",
        "global-exclude __pycache__",
        "global-exclude *.so"
    ]
    
    for pattern in required_patterns:
        assert pattern in content, f"MANIFEST.in missing pattern: {pattern}"


def test_wheel_contents():
    """Test wheel file contents."""
    try:
        # Build wheel
        subprocess.run(["poetry", "build", "-f", "wheel"], check=True)
        
        # Find wheel file
        wheel_file = next(Path("dist").glob("*.whl"))
        
        # Extract wheel contents
        import zipfile
        with zipfile.ZipFile(wheel_file) as wheel:
            files = wheel.namelist()
            
            # Check for required files
            assert any(f.endswith("METADATA") for f in files), "Wheel missing METADATA"
            assert any(f.endswith("WHEEL") for f in files), "Wheel missing WHEEL"
            assert any(f.endswith("RECORD") for f in files), "Wheel missing RECORD"
            
            # Check package contents
            assert any("adpa/__init__.py" in f for f in files), "Wheel missing package __init__.py"
            
            # Check metadata contents
            metadata_file = next(f for f in files if f.endswith("METADATA"))
            metadata = wheel.read(metadata_file).decode()
            
            assert "Metadata-Version: " in metadata
            assert "Name: adpa" in metadata
            assert "Version: " in metadata
            assert "Summary: " in metadata
            assert "Home-page: " in metadata
            assert "Author: " in metadata
            assert "License: " in metadata
            assert "Requires-Python: " in metadata
            
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Wheel build failed: {e}")


def test_sdist_contents():
    """Test source distribution contents."""
    try:
        # Build sdist
        subprocess.run(["poetry", "build", "-f", "sdist"], check=True)
        
        # Find sdist file
        sdist_file = next(Path("dist").glob("*.tar.gz"))
        
        # Extract sdist contents
        import tarfile
        with tarfile.open(sdist_file) as sdist:
            files = sdist.getnames()
            
            # Check for required files
            required_files = [
                "pyproject.toml",
                "README.md",
                "LICENSE",
                "CHANGELOG.md",
                "src/adpa/__init__.py",
                "tests",
                "docs"
            ]
            
            for required in required_files:
                assert any(f.endswith(required) for f in files), \
                    f"Source distribution missing: {required}"
            
            # Check that no unwanted files are included
            unwanted_patterns = [
                "__pycache__",
                "*.pyc",
                "*.pyo",
                "*.pyd",
                ".git",
                ".pytest_cache",
                "dist",
                "build"
            ]
            
            for pattern in unwanted_patterns:
                matching = [f for f in files if pattern in f]
                assert not matching, \
                    f"Source distribution contains unwanted files: {matching}"
            
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Source distribution build failed: {e}")


def test_dependency_constraints():
    """Test dependency version constraints."""
    pyproject_path = Path("pyproject.toml")
    with open(pyproject_path) as f:
        import toml
        pyproject = toml.load(f)
    
    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    
    # Check version constraint patterns
    for pkg, constraint in dependencies.items():
        if pkg == "python":
            continue
        
        if isinstance(constraint, str):
            # Should use caret requirements for flexibility
            assert constraint.startswith("^"), \
                f"Dependency {pkg} should use caret requirement"
            
            # Version should be specific enough
            version_parts = constraint.lstrip("^").split(".")
            assert len(version_parts) >= 2, \
                f"Dependency {pkg} version should be at least major.minor"


def test_python_compatibility():
    """Test Python version compatibility."""
    pyproject_path = Path("pyproject.toml")
    with open(pyproject_path) as f:
        import toml
        pyproject = toml.load(f)
    
    python_version = pyproject["tool"]["poetry"]["dependencies"]["python"]
    
    # Extract minimum version
    min_version = version.parse(python_version.lstrip("^"))
    
    # Check minimum version is reasonable
    assert min_version >= version.parse("3.8"), \
        "Minimum Python version should be at least 3.8"
    
    # Check version is not too restrictive
    assert min_version < version.parse("4.0"), \
        "Python version constraint should not exclude Python 3.x"

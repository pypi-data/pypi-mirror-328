"""Tests for PyPI package structure and requirements."""
import os
import re
import sys
import json
import toml
import subprocess
from pathlib import Path
import importlib.metadata
import pytest


def test_pyproject_toml_validity():
    """Test pyproject.toml structure and content."""
    pyproject_path = Path("pyproject.toml")
    assert pyproject_path.exists(), "pyproject.toml must exist"
    
    # Load and validate pyproject.toml
    pyproject = toml.load(pyproject_path)
    
    # Check build-system
    assert "build-system" in pyproject
    assert pyproject["build-system"]["requires"] == ["poetry-core>=1.0.0"]
    assert pyproject["build-system"]["build-backend"] == "poetry.core.masonry.api"
    
    # Check tool.poetry section
    poetry = pyproject["tool"]["poetry"]
    assert "name" in poetry
    assert "version" in poetry
    assert "description" in poetry
    assert "authors" in poetry
    assert "license" in poetry
    assert "readme" in poetry
    assert "packages" in poetry
    
    # Validate version format
    version_pattern = r'^\d+\.\d+\.\d+$'
    assert re.match(version_pattern, poetry["version"]), "Version must follow semantic versioning"


def test_package_metadata():
    """Test package metadata completeness."""
    pkg_name = "adpa"
    try:
        metadata = importlib.metadata.metadata(pkg_name)
        assert metadata["Name"] == pkg_name
        assert metadata["License"] == "MIT"
        assert all(key in metadata for key in [
            "Author", "Author-email", "License",
            "Description", "Keywords", "Classifier"
        ])
    except importlib.metadata.PackageNotFoundError:
        pytest.skip("Package not installed")


def test_required_files_exist():
    """Test presence of required package files."""
    required_files = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "pyproject.toml",
        "src/adpa/__init__.py",
        "tests/__init__.py"
    ]
    
    for file_path in required_files:
        assert Path(file_path).exists(), f"{file_path} must exist"


def test_version_consistency():
    """Test version number consistency across files."""
    # Get version from pyproject.toml
    pyproject = toml.load("pyproject.toml")
    pyproject_version = pyproject["tool"]["poetry"]["version"]
    
    # Get version from __init__.py
    init_file = Path("src/adpa/__init__.py")
    init_content = init_file.read_text()
    init_version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', init_content)
    assert init_version_match, "__version__ must be defined in __init__.py"
    init_version = init_version_match.group(1)
    
    # Get version from CHANGELOG.md
    changelog = Path("CHANGELOG.md").read_text()
    changelog_version_match = re.search(r'##\s*\[(\d+\.\d+\.\d+)\]', changelog)
    assert changelog_version_match, "Latest version must be documented in CHANGELOG.md"
    changelog_version = changelog_version_match.group(1)
    
    # Compare versions
    assert pyproject_version == init_version == changelog_version, "Versions must match across all files"


def test_package_structure():
    """Test package directory structure."""
    required_dirs = [
        "src/adpa",
        "tests",
        "docs"
    ]
    
    for dir_path in required_dirs:
        assert Path(dir_path).is_dir(), f"{dir_path} must be a directory"
    
    # Check src layout
    src_dir = Path("src/adpa")
    assert src_dir.is_dir(), "Package must use src layout"
    assert (src_dir / "__init__.py").exists(), "Package must have __init__.py"


def test_documentation_completeness():
    """Test documentation completeness."""
    docs_dir = Path("docs")
    assert docs_dir.exists(), "docs directory must exist"
    
    # Check mkdocs.yml
    mkdocs_file = Path("mkdocs.yml")
    assert mkdocs_file.exists(), "mkdocs.yml must exist"
    
    # Check API documentation
    api_docs = docs_dir / "api"
    assert api_docs.exists(), "API documentation must exist"


def test_dependency_specifications():
    """Test dependency specifications."""
    pyproject = toml.load("pyproject.toml")
    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    
    # Check Python version constraint
    assert "python" in dependencies
    python_version = dependencies["python"]
    assert python_version.startswith("^"), "Python version should use caret requirement"
    
    # Check core dependencies
    core_deps = ["pydantic", "sqlalchemy", "openai", "streamlit"]
    for dep in core_deps:
        assert dep in dependencies, f"{dep} must be specified in dependencies"
        assert dependencies[dep].startswith("^"), f"{dep} should use caret requirement"


def test_development_tools_configuration():
    """Test development tools configuration."""
    pyproject = toml.load("pyproject.toml")
    
    # Check black configuration
    assert "tool" in pyproject
    assert "black" in pyproject["tool"]
    black_config = pyproject["tool"]["black"]
    assert "line-length" in black_config
    assert "target-version" in black_config
    
    # Check isort configuration
    assert "isort" in pyproject["tool"]
    isort_config = pyproject["tool"]["isort"]
    assert "profile" in isort_config
    assert isort_config["profile"] == "black"
    
    # Check flake8 configuration
    assert "flake8" in pyproject["tool"]
    flake8_config = pyproject["tool"]["flake8"]
    assert "max-line-length" in flake8_config
    assert "max-complexity" in flake8_config


def test_package_build():
    """Test package build process."""
    try:
        # Clean any existing builds
        subprocess.run(["rm", "-rf", "dist/"], check=True)
        
        # Build package
        result = subprocess.run(
            ["poetry", "build"],
            check=True,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, "Package build must succeed"
        
        # Check build artifacts
        dist_dir = Path("dist")
        assert dist_dir.exists(), "dist directory must exist after build"
        
        # Should have both wheel and sdist
        wheel_files = list(dist_dir.glob("*.whl"))
        sdist_files = list(dist_dir.glob("*.tar.gz"))
        assert len(wheel_files) == 1, "Must produce exactly one wheel file"
        assert len(sdist_files) == 1, "Must produce exactly one sdist file"
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Package build failed: {e.stdout}\n{e.stderr}")


def test_package_installation():
    """Test package installation in a clean environment."""
    try:
        # Create a temporary virtual environment
        venv_dir = ".test_venv"
        subprocess.run(["python", "-m", "venv", venv_dir], check=True)
        
        # Activate virtual environment and install package
        pip_path = os.path.join(venv_dir, "Scripts" if sys.platform == "win32" else "bin", "pip")
        
        # Install the package
        subprocess.run(
            [pip_path, "install", "."],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Verify installation
        result = subprocess.run(
            [pip_path, "show", "adpa"],
            check=True,
            capture_output=True,
            text=True
        )
        assert "Name: adpa" in result.stdout
        
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Package installation failed: {e.stdout}\n{e.stderr}")
    
    finally:
        # Clean up
        import shutil
        shutil.rmtree(venv_dir, ignore_errors=True)


def test_package_imports():
    """Test that all public modules are importable."""
    import adpa
    
    # Test core modules
    from adpa import core
    from adpa.core import base, types, utils
    
    # Test LLM modules
    from adpa.llm import base as llm_base
    from adpa.llm import types as llm_types
    
    # Test database modules
    from adpa.database import models, operations
    
    # Verify __all__ in __init__.py
    assert hasattr(adpa, "__all__"), "__all__ must be defined in __init__.py"
    for module in adpa.__all__:
        assert hasattr(adpa, module), f"{module} must be importable from package root"


def test_license_compliance():
    """Test license compliance."""
    license_file = Path("LICENSE")
    assert license_file.exists(), "LICENSE file must exist"
    
    license_content = license_file.read_text()
    assert "MIT License" in license_content, "Must use MIT License"
    assert str(Path.cwd().name) in license_content, "Project name must be in LICENSE"
    assert str(Path.cwd().name) in license_content, "Current year must be in LICENSE"

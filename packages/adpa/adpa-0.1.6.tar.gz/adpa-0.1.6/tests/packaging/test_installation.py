"""Tests for package installation and dependency management."""
import os
import sys
import venv
import shutil
import subprocess
from pathlib import Path
import pytest
from typing import Generator


@pytest.fixture
def temp_venv(tmp_path) -> Generator[Path, None, None]:
    """Create a temporary virtual environment."""
    venv_dir = tmp_path / ".venv"
    venv.create(venv_dir, with_pip=True)
    
    # Get path to Python and pip in venv
    if sys.platform == "win32":
        python = venv_dir / "Scripts" / "python.exe"
        pip = venv_dir / "Scripts" / "pip.exe"
    else:
        python = venv_dir / "bin" / "python"
        pip = venv_dir / "bin" / "pip"
    
    # Upgrade pip
    subprocess.run([str(pip), "install", "--upgrade", "pip"], check=True)
    
    yield venv_dir
    
    # Cleanup
    shutil.rmtree(venv_dir)


def test_clean_install(temp_venv):
    """Test package installation in a clean environment."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install package
    result = subprocess.run(
        [str(pip), "install", "."],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Installation failed: {result.stderr}"
    
    # Verify installation
    result = subprocess.run(
        [str(pip), "list"],
        capture_output=True,
        text=True
    )
    assert "adpa" in result.stdout


def test_dependency_installation(temp_venv):
    """Test all dependencies are properly installed."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install package
    subprocess.run([str(pip), "install", "."], check=True)
    
    # Get installed packages
    result = subprocess.run(
        [str(pip), "freeze"],
        capture_output=True,
        text=True
    )
    installed = {
        line.split("==")[0].lower()
        for line in result.stdout.splitlines()
    }
    
    # Check core dependencies
    core_deps = {
        "pydantic",
        "sqlalchemy",
        "openai",
        "streamlit",
        "plotly",
        "pandas"
    }
    
    for dep in core_deps:
        assert dep.lower() in installed, f"Missing dependency: {dep}"


def test_optional_dependencies(temp_venv):
    """Test optional dependency groups."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install with dev dependencies
    subprocess.run(
        [str(pip), "install", ".[dev]"],
        check=True
    )
    
    # Get installed packages
    result = subprocess.run(
        [str(pip), "freeze"],
        capture_output=True,
        text=True
    )
    installed = {
        line.split("==")[0].lower()
        for line in result.stdout.splitlines()
    }
    
    # Check dev dependencies
    dev_deps = {
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pytest-xdist",
        "pytest-benchmark",
        "mypy"
    }
    
    for dep in dev_deps:
        assert dep.lower() in installed, f"Missing dev dependency: {dep}"


def test_dependency_conflicts(temp_venv):
    """Test for dependency conflicts."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install package
    subprocess.run([str(pip), "install", "."], check=True)
    
    # Check for dependency conflicts
    result = subprocess.run(
        [str(pip), "check"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Dependency conflicts found: {result.stdout}"


def test_minimal_installation(temp_venv):
    """Test installation with minimal dependencies."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    python = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "python"
    
    # Install only core package
    subprocess.run([str(pip), "install", "."], check=True)
    
    # Try importing core functionality
    result = subprocess.run(
        [str(python), "-c", "import adpa.core"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "Core functionality import failed"


def test_development_installation(temp_venv):
    """Test development installation mode."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install in development mode
    subprocess.run(
        [str(pip), "install", "-e", "."],
        check=True
    )
    
    # Verify development installation
    result = subprocess.run(
        [str(pip), "list", "--editable"],
        capture_output=True,
        text=True
    )
    assert "adpa" in result.stdout


def test_uninstall_cleanup(temp_venv):
    """Test package uninstallation cleanup."""
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    site_packages = list(temp_venv.glob("lib/*/site-packages"))[0]
    
    # Install package
    subprocess.run([str(pip), "install", "."], check=True)
    
    # Get installed files
    adpa_files = list(site_packages.glob("adpa*"))
    assert adpa_files, "No package files found"
    
    # Uninstall package
    subprocess.run([str(pip), "uninstall", "-y", "adpa"], check=True)
    
    # Check all files are removed
    remaining_files = list(site_packages.glob("adpa*"))
    assert not remaining_files, f"Files remaining after uninstall: {remaining_files}"


def test_package_size():
    """Test package size is reasonable."""
    # Build package
    subprocess.run(["poetry", "build"], check=True)
    
    # Check wheel size
    wheel = next(Path("dist").glob("*.whl"))
    wheel_size = wheel.stat().st_size
    
    # Wheel should be less than 10MB
    MAX_WHEEL_SIZE = 10 * 1024 * 1024  # 10MB
    assert wheel_size <= MAX_WHEEL_SIZE, \
        f"Wheel size ({wheel_size} bytes) exceeds {MAX_WHEEL_SIZE} bytes"


def test_install_time(temp_venv):
    """Test package installation time is reasonable."""
    import time
    pip = temp_venv / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Time the installation
    start_time = time.time()
    subprocess.run([str(pip), "install", "."], check=True)
    install_time = time.time() - start_time
    
    # Installation should take less than 5 minutes
    MAX_INSTALL_TIME = 300  # 5 minutes
    assert install_time <= MAX_INSTALL_TIME, \
        f"Installation time ({install_time}s) exceeds {MAX_INSTALL_TIME}s"

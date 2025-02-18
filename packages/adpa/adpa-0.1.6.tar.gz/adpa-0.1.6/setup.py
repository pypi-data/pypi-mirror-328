"""ADPA Framework setup configuration."""
from pathlib import Path
from setuptools import setup, find_packages

def read_version():
    with open(Path(__file__).parent / "src" / "adpa" / "VERSION", "r") as f:
        return f.read().strip()

def read_requirements(filename):
    with open(Path(__file__).parent / filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="adpa",
    version="0.1.0",
    author="ADPA Team",
    author_email="info@adpa.io",
    description="Advanced Data Processing and Analytics Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adpa/adpa",
    project_urls={
        "Bug Tracker": "https://github.com/adpa/adpa/issues",
        "Documentation": "https://adpa.readthedocs.io/",
        "Source Code": "https://github.com/adpa/adpa",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Framework :: Jupyter",
        "Framework :: FastAPI",
        "Typing :: Typed",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "sqlalchemy>=2.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.22.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "aiohttp>=3.8.0",
        "asyncio>=3.4.3",
        "typing-extensions>=4.7.0",
        "click>=8.1.0",
        "rich>=13.4.0",
        "tqdm>=4.65.0",
        "loguru>=0.7.0",
        "prometheus-client>=0.17.0",
        "opentelemetry-api>=1.19.0",
        "opentelemetry-sdk>=1.19.0",
        "cryptography>=41.0.0",
        "pyjwt>=2.8.0",
        "bcrypt>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.0",
            "pytest-xdist>=3.3.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.4.0",
            "flake8>=6.1.0",
            "pylint>=2.17.0",
            "bandit>=1.7.0",
            "pre-commit>=3.3.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
            "mkdocstrings>=0.23.0",
            "mkdocstrings-python>=1.7.0",
            "mkdocs-jupyter>=0.24.0",
            "mkdocs-git-revision-date-plugin>=0.3.0",
            "mkdocs-git-authors-plugin>=0.7.0",
            "mkdocs-minify-plugin>=0.7.0",
            "mkdocs-redirects>=1.2.0",
            "mkdocs-awesome-pages-plugin>=2.9.0",
            "mkdocs-include-markdown-plugin>=6.0.0",
            "mkdocs-macros-plugin>=1.0.0",
            "plantuml-markdown>=3.9.0",
            "pymdown-extensions>=10.3.0",
            "pygments>=2.16.0",
            "cairosvg>=2.7.0",
            "pillow>=10.0.0",
        ],
        "test": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.0",
            "pytest-xdist>=3.3.0",
            "coverage>=7.3.0",
            "tox>=4.6.0",
        ],
        "lint": [
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.4.0",
            "flake8>=6.1.0",
            "pylint>=2.17.0",
            "bandit>=1.7.0",
        ],
        "security": [
            "bandit>=1.7.0",
            "safety>=2.3.0",
            "cryptography>=41.0.0",
            "pyopenssl>=23.2.0",
            "certifi>=2023.7.22",
        ],
        "all": [
            "adpa[dev,docs,test,lint,security]",
        ],
    },
    entry_points={
        "console_scripts": [
            "adpa=adpa.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "adpa": [
            "py.typed",
            "*.pyi",
            "**/*.pyi",
        ],
    },
    zip_safe=False,
)

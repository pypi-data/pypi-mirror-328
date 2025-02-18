"""Test Data Management System for ADPA Framework."""
import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml
from faker import Faker

class TestDataManager:
    """Manages test data across different test categories."""

    def __init__(self, base_dir: Optional[str] = None):
        """Initialize TestDataManager.
        
        Args:
            base_dir: Base directory for test data storage. Defaults to tests/data.
        """
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent / "data"
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.faker = Faker()
        self.version_file = self.base_dir / "versions.json"
        self._load_versions()

    def _load_versions(self) -> None:
        """Load version information from versions.json."""
        if self.version_file.exists():
            with open(self.version_file, "r") as f:
                self.versions = json.load(f)
        else:
            self.versions = {}

    def _save_versions(self) -> None:
        """Save version information to versions.json."""
        with open(self.version_file, "w") as f:
            json.dump(self.versions, f, indent=2)

    def get_test_data(self, category: str, scenario: str, version: Optional[str] = None) -> Dict[str, Any]:
        """Get test data for a specific scenario.
        
        Args:
            category: Test category (e.g., 'api', 'database', 'llm')
            scenario: Test scenario name
            version: Specific version to retrieve. Defaults to latest.
        
        Returns:
            Dict containing test data
        """
        data_dir = self.base_dir / category
        if not version:
            version = self.versions.get(f"{category}/{scenario}", "latest")
        
        data_file = data_dir / f"{scenario}_v{version}.yaml"
        if not data_file.exists():
            raise FileNotFoundError(f"Test data not found: {data_file}")
        
        with open(data_file, "r") as f:
            return yaml.safe_load(f)

    def save_test_data(self, category: str, scenario: str, data: Dict[str, Any]) -> str:
        """Save test data for a specific scenario.
        
        Args:
            category: Test category
            scenario: Test scenario name
            data: Test data to save
        
        Returns:
            Version string of saved data
        """
        data_dir = self.base_dir / category
        data_dir.mkdir(parents=True, exist_ok=True)

        # Generate new version
        key = f"{category}/{scenario}"
        current = self.versions.get(key, "0.0")
        major, minor = map(int, current.split("."))
        new_version = f"{major}.{minor + 1}"
        self.versions[key] = new_version

        # Save data
        data_file = data_dir / f"{scenario}_v{new_version}.yaml"
        with open(data_file, "w") as f:
            yaml.dump(data, f, sort_keys=False)

        self._save_versions()
        return new_version

    def generate_test_data(self, category: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Generate test data based on schema.
        
        Args:
            category: Test category
            schema: Data schema with Faker providers
        
        Returns:
            Generated test data
        """
        def _generate_value(field_type: str, **kwargs) -> Any:
            if hasattr(self.faker, field_type):
                return getattr(self.faker, field_type)(**kwargs)
            raise ValueError(f"Unknown field type: {field_type}")

        generated_data = {}
        for field, field_info in schema.items():
            if isinstance(field_info, dict):
                field_type = field_info.pop("type")
                generated_data[field] = _generate_value(field_type, **field_info)
            else:
                generated_data[field] = _generate_value(field_info)

        return generated_data

    def cleanup_test_data(self, category: Optional[str] = None, keep_versions: int = 3) -> None:
        """Clean up old test data versions.
        
        Args:
            category: Optional category to clean. If None, cleans all categories.
            keep_versions: Number of recent versions to keep per scenario.
        """
        def _cleanup_category(cat_dir: Path) -> None:
            scenarios = {}
            for data_file in cat_dir.glob("*_v*.yaml"):
                scenario = data_file.stem.split("_v")[0]
                version = data_file.stem.split("_v")[1]
                scenarios.setdefault(scenario, []).append((version, data_file))

            for scenario_files in scenarios.values():
                # Sort by version number
                sorted_files = sorted(scenario_files, 
                                   key=lambda x: [int(n) for n in x[0].split(".")])
                # Remove old versions
                for _, file_path in sorted_files[:-keep_versions]:
                    file_path.unlink()

        if category:
            cat_dir = self.base_dir / category
            if cat_dir.exists():
                _cleanup_category(cat_dir)
        else:
            for cat_dir in self.base_dir.iterdir():
                if cat_dir.is_dir():
                    _cleanup_category(cat_dir)

    def export_test_data(self, export_dir: Union[str, Path]) -> None:
        """Export all test data to a directory.
        
        Args:
            export_dir: Directory to export data to
        """
        export_path = Path(export_dir)
        export_path.mkdir(parents=True, exist_ok=True)
        
        # Copy all data files
        shutil.copytree(self.base_dir, export_path, dirs_exist_ok=True)
        
        # Create manifest
        manifest = {
            "exported_at": datetime.now().isoformat(),
            "versions": self.versions,
            "categories": [d.name for d in self.base_dir.iterdir() if d.is_dir()]
        }
        
        with open(export_path / "manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)

    def import_test_data(self, import_dir: Union[str, Path]) -> None:
        """Import test data from a directory.
        
        Args:
            import_dir: Directory containing exported test data
        """
        import_path = Path(import_dir)
        if not import_path.exists():
            raise FileNotFoundError(f"Import directory not found: {import_path}")
            
        # Verify manifest
        manifest_file = import_path / "manifest.json"
        if not manifest_file.exists():
            raise FileNotFoundError("Manifest file not found in import directory")
            
        # Copy data files
        shutil.copytree(import_path, self.base_dir, dirs_exist_ok=True)
        
        # Update versions
        self._load_versions()

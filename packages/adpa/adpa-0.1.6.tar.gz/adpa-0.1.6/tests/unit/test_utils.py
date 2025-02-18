import unittest
import os
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from adpa.utils.testing import parse_robot_results
from adpa.utils.file_utils import get_project_root, ensure_dir

class TestUtils(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path("test_data")
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self):
        """Clean up test environment."""
        import shutil
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_parse_robot_results_empty(self):
        """Test parsing empty or non-existent robot results."""
        result = parse_robot_results("nonexistent.xml")
        self.assertIsNone(result)

    def test_parse_robot_results_invalid(self):
        """Test parsing invalid XML."""
        invalid_xml = self.test_dir / "invalid.xml"
        invalid_xml.write_text("<invalid>")
        result = parse_robot_results(str(invalid_xml))
        self.assertIsNone(result)

    def test_parse_robot_results_valid(self):
        """Test parsing valid robot results."""
        # Create a minimal valid robot results XML
        valid_xml = self.test_dir / "output.xml"
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <robot generated="20240104 10:58:28.789" generator="Robot 6.1.1 (Python 3.11.0 on win32)">
            <statistics>
                <total>
                    <stat pass="2" fail="1">All Tests</stat>
                </total>
            </statistics>
            <suite>
                <status status="PASS" starttime="20240104 10:58:28.789" endtime="20240104 10:58:29.789"/>
            </suite>
        </robot>
        """
        valid_xml.write_text(xml_content)
        
        result = parse_robot_results(str(valid_xml))
        self.assertIsNotNone(result)
        stats, tests = result
        
        # Verify stats
        self.assertEqual(stats['total'], 3)
        self.assertEqual(stats['passed'], 2)
        self.assertEqual(stats['failed'], 1)

    def test_get_project_root(self):
        """Test project root detection."""
        root = get_project_root()
        self.assertTrue(root.exists())
        self.assertTrue((root / "adpa").exists())

    def test_ensure_dir(self):
        """Test directory creation."""
        # Test single directory
        test_path = self.test_dir / "new_dir"
        ensure_dir(test_path)
        self.assertTrue(test_path.exists())
        
        # Test nested directories
        nested_path = self.test_dir / "parent" / "child" / "grandchild"
        ensure_dir(nested_path)
        self.assertTrue(nested_path.exists())
        
        # Test with file path
        file_path = self.test_dir / "parent" / "test.txt"
        ensure_dir(file_path)
        self.assertTrue(file_path.parent.exists())

    def test_robot_results_edge_cases(self):
        """Test robot results parsing edge cases."""
        # Test with minimal valid XML
        minimal_xml = self.test_dir / "minimal.xml"
        minimal_content = """<?xml version="1.0" encoding="UTF-8"?>
        <robot>
            <statistics>
                <total>
                    <stat>All Tests</stat>
                </total>
            </statistics>
        </robot>
        """
        minimal_xml.write_text(minimal_content)
        result = parse_robot_results(str(minimal_xml))
        self.assertIsNotNone(result)
        
        # Test with missing statistics
        no_stats_xml = self.test_dir / "no_stats.xml"
        no_stats_content = """<?xml version="1.0" encoding="UTF-8"?>
        <robot>
            <suite>
                <test name="Test 1">
                    <status status="PASS"/>
                </test>
            </suite>
        </robot>
        """
        no_stats_xml.write_text(no_stats_content)
        result = parse_robot_results(str(no_stats_xml))
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

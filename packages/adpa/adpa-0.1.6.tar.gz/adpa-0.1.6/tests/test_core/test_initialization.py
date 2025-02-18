import pytest
from pathlib import Path
import re

def test_documentation_urls():
    """Test that all documentation URLs point to the correct repository"""
    project_root = Path(__file__).parent.parent.parent
    correct_repo = "achimdehnert/ADPA"
    files_to_check = {
        'docs/index.md': [
            r'https://github\.com/[^/]+/ADPA',  # Any GitHub links
            r'http://localhost:8505'  # Streamlit port
        ],
        'docs/quickstart.md': [
            r'git clone https://github\.com/[^/]+/ADPA\.git'
        ],
        'docs/setup_guide.md': [
            r'git clone https://github\.com/[^/]+/ADPA\.git'
        ],
        'streamlit_app/Home.py': [
            r'https://github\.com/[^/]+/ADPA/blob/main/docs/[^)]+\)'
        ],
        'mkdocs.yml': [
            r'site_url: https://github\.com/[^/]+/ADPA',
            r'repo_url: https://github\.com/[^/]+/ADPA',
            r'repo_name: [^/]+/ADPA'
        ]
    }
    
    for file_path, patterns in files_to_check.items():
        print(f"\nChecking {file_path}...")
        try:
            file_content = (project_root / file_path).read_text(encoding='utf-8')
            for pattern in patterns:
                matches = list(re.finditer(pattern, file_content))
                if not matches:
                    print(f"[WARNING] No matches found for pattern {pattern}")
                for match in matches:
                    url = match.group(0)
                    print(f"Found URL: {url}")
                    if 'localhost' not in url:  # Skip localhost URL checks
                        assert correct_repo in url, f"Incorrect repository URL in {file_path}: {url}"
            print(f"[OK] All URLs in {file_path} are correct")
        except FileNotFoundError:
            print(f"[WARNING] File not found: {file_path}")
        except Exception as e:
            print(f"[ERROR] Error checking {file_path}: {str(e)}")
            raise

if __name__ == "__main__":
    test_documentation_urls()

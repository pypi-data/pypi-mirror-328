"""File utility functions for the ADPA Framework."""

import os
from pathlib import Path
from typing import Union, Optional, List, Iterator
import shutil

def get_project_root() -> Path:
    """Get the project root directory.
    
    Returns:
        Path: The absolute path to the project root directory
    """
    current = Path(__file__).resolve()
    while current.name.lower() != "adpa" and current.parent != current:
        current = current.parent
    return current

def ensure_dir(path: Union[str, Path]) -> Path:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Path to the directory to ensure exists
        
    Returns:
        Path: The path to the ensured directory
    """
    path = Path(path)
    if path.suffix:  # If path includes a file name
        path = path.parent
    path.mkdir(parents=True, exist_ok=True)
    return path

def safe_file_write(path: Union[str, Path], content: str, mode: str = 'w', encoding: str = 'utf-8') -> None:
    """Safely write content to a file, ensuring the directory exists.
    
    Args:
        path: Path to the file to write
        content: Content to write to the file
        mode: File open mode (default: 'w')
        encoding: File encoding (default: 'utf-8')
    """
    path = Path(path)
    ensure_dir(path)
    with open(path, mode, encoding=encoding) as f:
        f.write(content)

def find_files(
    directory: Union[str, Path], 
    pattern: str,
    recursive: bool = True,
    exclude_dirs: Optional[List[str]] = None
) -> List[Path]:
    """Find all files matching a pattern in a directory.
    
    Args:
        directory: Directory to search in
        pattern: Glob pattern to match files against
        recursive: Whether to search recursively (default: True)
        exclude_dirs: List of directory names to exclude (default: None)
        
    Returns:
        list[Path]: List of matching file paths
    """
    directory = Path(directory)
    exclude_dirs = exclude_dirs or ['.git', '__pycache__', '.pytest_cache']
    
    def _is_excluded(path: Path) -> bool:
        return any(part in exclude_dirs for part in path.parts)
    
    if recursive:
        matches = directory.rglob(pattern)
    else:
        matches = directory.glob(pattern)
    
    return [p for p in matches if not _is_excluded(p)]

def get_relative_path(path: Union[str, Path], relative_to: Optional[Union[str, Path]] = None) -> Path:
    """Get a path relative to another path or the project root.
    
    Args:
        path: Path to make relative
        relative_to: Path to make relative to (default: project root)
        
    Returns:
        Path: The relative path
    """
    path = Path(path)
    if relative_to is None:
        relative_to = get_project_root()
    return path.relative_to(Path(relative_to))

def is_binary_file(file_path: Union[str, Path], sample_size: int = 1024) -> bool:
    """Check if a file is binary.
    
    Args:
        file_path: Path to the file to check
        sample_size: Number of bytes to check (default: 1024)
        
    Returns:
        bool: True if the file is binary, False otherwise
    """
    try:
        with open(file_path, 'tr', encoding='utf-8') as f:
            f.read(sample_size)
        return False
    except UnicodeDecodeError:
        return True

def safe_file_copy(src: Union[str, Path], dst: Union[str, Path], overwrite: bool = False) -> None:
    """Safely copy a file, ensuring the destination directory exists.
    
    Args:
        src: Source file path
        dst: Destination file path
        overwrite: Whether to overwrite existing files (default: False)
    
    Raises:
        FileExistsError: If the destination file exists and overwrite is False
        FileNotFoundError: If the source file doesn't exist
    """
    src, dst = Path(src), Path(dst)
    if not src.exists():
        raise FileNotFoundError(f"Source file not found: {src}")
    if dst.exists() and not overwrite:
        raise FileExistsError(f"Destination file exists: {dst}")
    
    ensure_dir(dst)
    shutil.copy2(src, dst)

def safe_file_move(src: Union[str, Path], dst: Union[str, Path], overwrite: bool = False) -> None:
    """Safely move a file, ensuring the destination directory exists.
    
    Args:
        src: Source file path
        dst: Destination file path
        overwrite: Whether to overwrite existing files (default: False)
    
    Raises:
        FileExistsError: If the destination file exists and overwrite is False
        FileNotFoundError: If the source file doesn't exist
    """
    src, dst = Path(src), Path(dst)
    if not src.exists():
        raise FileNotFoundError(f"Source file not found: {src}")
    if dst.exists() and not overwrite:
        raise FileExistsError(f"Destination file exists: {dst}")
    
    ensure_dir(dst)
    shutil.move(str(src), str(dst))

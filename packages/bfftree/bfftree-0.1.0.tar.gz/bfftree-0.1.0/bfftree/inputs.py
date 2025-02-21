"""Input functions for creating BFFTrees from various sources."""
import json

from typing import List
import pathlib
import lzma
from remotezip import RemoteZip # type: ignore
from fs.ftpfs import FTPFS # type: ignore
from pydantic import BaseModel

from .tree import RadixTreeNode


class FileEntry(BaseModel):
    path: str
    size: int


def load_file_entries(json_path: str) -> List[FileEntry]:
    """
    Load and parse JSON file containing file entries into Pydantic models
    
    Args:
        json_path: Path to the JSON file
        
    Returns:
        List of FileEntry objects
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    return [FileEntry(**entry) for entry in data]


def build_radix_tree(entries: List[FileEntry]) -> RadixTreeNode:
    """
    Build a radix tree from a list of FileEntry objects.
    
    Args:
        entries: List of FileEntry objects
        
    Returns:
        Root node of the radix tree
    """
    root = RadixTreeNode()
    for entry in entries:
        root.insert(entry.path, entry.size)
    return root


def read_biostudies(json_path: str) -> RadixTreeNode:
    """Read a BioStudies JSON file and return its radix tree.
    
    Args:
        json_path: Path to the JSON file
        
    Returns:
        RadixTree representation of the file hierarchy
    """
    entries = load_file_entries(json_path)
    return build_radix_tree(entries)


def remote_zip_to_bfftree(zip_url: str) -> RadixTreeNode:
    """Create a BFFTree from a remote zip file.
    
    Args:
        zip_url: URL of the zip file to process
        
    Returns:
        RadixTree representation of the zip contents
    """
    entries = []
    
    with RemoteZip(zip_url) as zip:
        for zip_info in zip.infolist():
            if not zip_info.is_dir():  # Skip directory entries
                entries.append(FileEntry(
                    path=zip_info.filename,
                    size=zip_info.file_size
                ))
    
    return build_radix_tree(entries)


def empiar_entry_to_bfftree(accession_id: str) -> RadixTreeNode:
    """Create a BFFTree from an EMPIAR entry.
    
    Args:
        accession_id: EMPIAR accession ID (e.g. "EMPIAR-12105")
        
    Returns:
        RadixTree representation of the EMPIAR entry
    """
    # Parse accession number from ID (e.g. "EMPIAR-12105" -> "12105")
    accession_no = accession_id.split('-')[-1]
    
    ftp_fs = FTPFS('ftp.ebi.ac.uk')
    root_path = f"/empiar/world_availability/{accession_no}/data"
    
    all_files = []
    
    # Walk the FTP directory structure
    walker = ftp_fs.walk(root_path)
    for path, dirs, files in walker:
        for file in files:
            relpath = pathlib.Path(path).relative_to(root_path)
            empiar_file = FileEntry(
                path=str(relpath/file.name),
                size=file.size
            )
            all_files.append(empiar_file)
    
    return build_radix_tree(all_files)

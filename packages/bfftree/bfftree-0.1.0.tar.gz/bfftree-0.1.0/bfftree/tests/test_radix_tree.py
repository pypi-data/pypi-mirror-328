import pytest
from bfftree import RadixTreeNode

def test_empty_tree():
    """Test an empty tree has zero size"""
    tree = RadixTreeNode()
    assert tree.size == 0
    assert tree.get_size() == 0
    assert tree.edges == []

def test_single_file():
    """Test inserting a single file"""
    tree = RadixTreeNode()
    tree.insert("test.txt", 100)
    
    assert tree.get_size() == 100
    paths = tree.get_all_paths()
    assert len(paths) == 1
    assert paths[0] == ("test.txt", 100)

def test_nested_files():
    """Test inserting nested files"""
    tree = RadixTreeNode()
    tree.insert("dir1/file1.txt", 100)
    tree.insert("dir1/file2.txt", 200)
    tree.insert("dir2/file3.txt", 300)
    
    assert tree.get_size() == 600
    
    # Test finding specific nodes
    dir1 = tree.find_node("dir1")
    assert dir1 is not None
    assert dir1.get_size() == 300
    
    dir2 = tree.find_node("dir2")
    assert dir2 is not None
    assert dir2.get_size() == 300
    
    # Test all paths are found
    paths = tree.get_all_paths()
    assert len(paths) == 3
    assert ("dir1/file1.txt", 100) in paths
    assert ("dir1/file2.txt", 200) in paths
    assert ("dir2/file3.txt", 300) in paths

def test_nonexistent_path():
    """Test finding a path that doesn't exist"""
    tree = RadixTreeNode()
    tree.insert("dir1/file1.txt", 100)
    
    assert tree.find_node("nonexistent") is None
    assert tree.find_node("dir1/nonexistent") is None

def test_empty_path():
    """Test operations with empty paths"""
    tree = RadixTreeNode()
    
    # Empty path should return the root node
    assert tree.find_node("") == tree
    
    # Insert with empty path should set root node size
    tree.insert("", 100)
    assert tree.size == 100

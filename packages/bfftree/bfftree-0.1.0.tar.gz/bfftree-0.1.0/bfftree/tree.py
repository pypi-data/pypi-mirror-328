from typing import List, Optional, Dict, Any, Tuple
import json
from bfftree.bettertree_pb2 import RadixTreeNode as ProtoNode, RadixTreeEdge as ProtoEdge


class RadixTreeNode:
    """A node in a radix tree representing file paths and their sizes."""
    def __init__(self, size: int = 0):
        self.size: int = size
        self.edges: List[Tuple[str, 'RadixTreeNode']] = []

    def insert(self, path: str, size: int):
        """Insert a path and its size into the radix tree."""
        if not path:
            self.size = size
            return

        segments = path.split('/')
        current = self
        
        for segment in segments:
            # Look for matching edge
            found = False
            for i, (edge_label, child) in enumerate(current.edges):
                if edge_label == segment:
                    current = child
                    found = True
                    break
            
            if not found:
                # Create new edge and node
                new_node = RadixTreeNode()
                current.edges.append((segment, new_node))
                current = new_node
        
        current.size = size

    def get_size(self) -> int:
        """Get total size of this node and all its children."""
        total = self.size
        for _, child in self.edges:
            total += child.get_size()
        return total

    def find_node(self, path: str) -> Optional['RadixTreeNode']:
        """Find a node by its path."""
        if not path:
            return self

        segments = path.split('/')
        current = self

        for segment in segments:
            found = False
            for edge_label, child in current.edges:
                if edge_label == segment:
                    current = child
                    found = True
                    break
            if not found:
                return None

        return current

    def get_all_paths(self, prefix: str = "") -> List[Tuple[str, int]]:
        """Get all file paths and sizes in the tree."""
        paths = []
        if self.size > 0:  # This is a file
            paths.append((prefix, self.size))
        
        for edge_label, child in self.edges:
            new_prefix = f"{prefix}/{edge_label}" if prefix else edge_label
            paths.extend(child.get_all_paths(new_prefix))
        
        return paths

    def to_dict(self) -> Dict[str, Any]:
        """Convert the node and its children to a dictionary."""
        result = {
            "size": self.size,
            "edges": []
        }
        for edge_label, child in self.edges:
            result["edges"].append({
                "label": edge_label,
                "node": child.to_dict()
            })
        return result

    def save_to_file(self, filepath: str):
        """Save the radix tree to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    def to_proto(self) -> ProtoNode:
        """Convert the node and its children to a protobuf message."""
        proto_node = ProtoNode()
        proto_node.size = self.size
        
        for edge_label, child in self.edges:
            edge = proto_node.children.add()
            edge.edge_label = edge_label
            edge.child.CopyFrom(child.to_proto())
            
        return proto_node

    def save_to_proto_file(self, filepath: str):
        """Save the radix tree to a protobuf file."""
        with open(filepath, 'wb') as f:
            f.write(self.to_proto().SerializeToString())

    @classmethod
    def load_from_proto_file(cls, filepath: str) -> 'RadixTreeNode':
        """Load a radix tree from a protobuf file."""
        proto_node = ProtoNode()
        with open(filepath, 'rb') as f:
            proto_node.ParseFromString(f.read())
        return cls.load_from_proto_file_proto(proto_node)

    @classmethod
    def load_from_proto_file_proto(cls, proto_node: ProtoNode) -> 'RadixTreeNode':
        """Helper method to recursively load nodes from proto messages."""
        node = cls(proto_node.size)
        for edge in proto_node.children:
            child = cls.load_from_proto_file_proto(edge.child)
            node.edges.append((edge.edge_label, child))
        return node

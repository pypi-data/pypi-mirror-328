"""
This module provides the TreeNode class, which is the fundamental building block
for binary tree data structures. It implements a simple node interface with value
and left/right child pointers.
"""

from typing import TypeVar, Optional, Any
from dataclasses import dataclass

# enforces consistency of tree root and node values
T = TypeVar('T')

@dataclass
class TreeNode:
    """
    A class representing a node in a binary tree.

    Attributes:
        value: The value stored in the node
        left: Reference to the left child node (None if no left child)
        right: Reference to the right child node (None if no right child)
    """
    value: T
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

def validate_tree_node(node: Any):
    """Validate that a node implements the minimum tree node interface.
    
    Args:
        node: Any object to check as a tree node

    Raises:
        AttributeError: If the node does not have the required attributes
    """
    if node is not None:
        if not hasattr(node, 'value'):
            raise AttributeError("Node must have a 'value' attribute")
        if not hasattr(node, 'left'):
            raise AttributeError("Node must have a 'left' attribute")
        if not hasattr(node, 'right'):
            raise AttributeError("Node must have a 'right' attribute")

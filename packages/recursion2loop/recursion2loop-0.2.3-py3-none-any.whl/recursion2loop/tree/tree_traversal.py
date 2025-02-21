"""
This module provides iterative implementations of common binary tree traversal algorithms.
It includes inorder, preorder, postorder, and level-order traversal methods.
"""

from typing import Optional
from .tree_node import TreeNode, validate_tree_node, T

def inorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative inorder traversal of a binary tree.
    Inorder traversal visits nodes in the order: left subtree, root, right subtree.
    This is commonly used to visit binary tree nodes in ascending order.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in inorder traversal order
    """
    if not root:
        return []

    validate_tree_node(root)

    stack = []
    result = []

    while root or stack:
        # Traverse to leftmost node
        while root:
            stack.append(root)
            root = root.left

        # Process current node and move to right subtree
        root = stack.pop()
        result.append(root.value)
        root = root.right

    return result


def preorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative preorder traversal of a binary tree.
    Preorder traversal visits nodes in the order: root, left subtree, right subtree.
    This traversal is useful for creating a copy of the tree or serializing tree structure.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in preorder traversal order
    """
    if not root:
        return []

    validate_tree_node(root)

    stack = [root]
    result = []

    while stack:
        # Process current node
        node = stack.pop()
        result.append(node.value)

        # Push right child first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative postorder traversal of a binary tree.
    Postorder traversal visits nodes in the order: left subtree, right subtree, root.
    This is useful when deleting nodes or evaluating mathematical expressions.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in postorder traversal order
    """
    if not root:
        return []

    stack = [root]
    result = []

    validate_tree_node(root)

    while stack:
        # Modified preorder traversal (root, right, left)
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reverse to get postorder (left, right, root)
    return result[::-1]

def level_order_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative level order traversal of a binary tree.
    Level order traversal visits nodes level by level from left to right.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in level order traversal order
    """
    if not root:
        return []

    validate_tree_node(root)

    stack = [root]
    result = []

    while stack:
        node = stack.pop(0)
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result

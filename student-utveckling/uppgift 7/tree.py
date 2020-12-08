# encoding: iso-8859-1

# TDDE23 Lab 4: Binary tree

def is_empty_tree(tree):
    """Returns true if tree is empty"""
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    """Returns true if tree i a leaf"""
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    """Creates a tree"""
    return [left_tree, key, right_tree]


def left_subtree(tree):
    """Returns the left subtree"""
    return tree[0]


def right_subtree(tree):
    """Returns the right subtree"""
    return tree[2]

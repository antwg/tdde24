#hjälpfuktioner från labb 4
from tree import *

#fuktioner som står i uppgiften
def empty_tree_fn():
    return 0

def leaf_fn(key):
    # print('leaf', key)
    return key**2

def inner_node_fn(key, left_value, right_value):
    # print('node', key, 'left', left_value, 'right', right_value)
    return key + left_value

#definerad själv
def is_inner_node(tree):
    if len(tree) == 3\
    and isinstance(left_subtree(tree), (int, list))\
    and isinstance(right_subtree(tree), (int, list)):
        return True

    else:
        return False

def return_key(tree):
    return tree[1]

#main fuction
def traverse(tree, inner_node_func, leaf_func, empty_tree_func):
    """Traverses a tree and performs different tasks depending on input funtions"""
    if is_empty_tree(tree):
        return empty_tree_func()

    elif is_leaf(tree):
        return leaf_func(tree)

    elif is_inner_node(tree):
        left = traverse(left_subtree(tree), inner_node_func, leaf_func,
                        empty_tree_func)
        right = traverse(right_subtree(tree), inner_node_func, leaf_func,
                        empty_tree_func)

        return inner_node_func(return_key(tree), left, right)


def contains_key(key: int, tree: list) -> bool:
    """Checks if a tree contains a given key"""
    def inner_node_func(tree, left, right):
        """Returns true if left or right returns true, else false"""
        return tree == key or left or right

    def leaf_func(tree):
        """Returns true if leaf = key, else false"""
        return tree == key

    def empty_tree_func():
        """Returns false if tree is empty"""
        return False

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)


def tree_depth(tree):
    """Returns the depth of a given tree"""
    def inner_node_func(tree, left, right):
        """Returns the larget of the two branches and adds 1"""
        return max(left, right) + 1

    def leaf_func(tree):
        """Returns 1 for leaf"""
        return 1

    def empty_tree_func():
        """Returns 0 if tree is empty"""
        return 0

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)



def tree_size(tree):
    """Returns the size of a given tree"""
    def inner_node_func(tree, left, right):
        """
        return the left and right subtree and value. Adds 1 because an inner
        node counts as a tree size
        """
        return left + right + 1

    def leaf_func(tree):
        """return a 1 because a leaf is a tree size """
        return 1

    def empty_tree_func():
        """return a 0 becuase an empty tree does not count as a size"""
        return 0

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)

def test():
    #test for traverse
    test_1_traverse = traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn)
    test_2_traverse = traverse([[4, 5, 6], 7, [[],8, 9]], inner_node_fn, leaf_fn, empty_tree_fn)
    test_3_traverse = traverse([], inner_node_fn, leaf_fn, empty_tree_fn)

    assert test_1_traverse == 43
    assert test_2_traverse == 28
    assert test_3_traverse == 0

    #test for contains_key
    test_key_1 = contains_key(7, [5, 7, 9])
    test_key_2 = contains_key(4, [5, 7, [[4, 5, 6], 9, 12]])
    test_key_3 = contains_key(13, [5, 7, [[4, 5, 6], 9, 12]])

    assert test_key_1 == True
    assert test_key_2 == True
    assert test_key_3 == False

    #test for tree depth
    test_1_depth = tree_depth(3)
    test_2_depth = tree_depth(([1,2,[2,3,4]], 5, [[6,7,8], 9, [10,11,[13, 14, 15]]]))
    test_3_depth = tree_depth([])

    assert test_1_depth == 1
    assert test_2_depth == 5
    assert test_3_depth == 0

    #test for tree size
    size_test_1 = tree_size([6, 8, []])
    size_test_2 = tree_size([])
    size_test_3 = tree_size([[4, 6, []], 7, [[], 9, 10]])

    assert size_test_1 == 2
    assert size_test_2 == 0
    assert size_test_3 == 5

    print('The code passed the test')

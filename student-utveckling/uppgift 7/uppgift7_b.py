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

# print(traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn))
# print(traverse([[4, 5, 6], 7, [[],8, 9]], inner_node_fn, leaf_fn, empty_tree_fn))


def contains_key(key: int, tree: list) -> bool:
    def inner_node_func(tree, left, right):
        return left or right

    def leaf_func(tree):
        return tree == key

    def empty_tree_func():
        return False

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)

# print(contains_key(5, [5, 7, 9]))
# print(contains_key(4, [5, 7, [[4, 5, 6], 9, 12]]))
# print(contains_key(13, [5, 7, [[4, 5, 6], 9, 12]]))

def tree_depth(tree):
    def inner_node_func(tree, left, right):
        return max(left, right) + 1

    def leaf_func(tree):
        return 1

    def empty_tree_func():
        return 0

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)

# print(tree_depth(3))
# print(tree_depth(([1,2,[2,3,4]], 5, [[6,7,8], 9, [10,11,[13, 14, 15]]])))

def tree_size(tree):
    def inner_node_func(tree, left, right):
        return left + right + 1

    def leaf_func(tree):
        return 1

    def empty_tree_func():
        return 0

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)

# print(tree_size([2, 7, []]))
# print(tree_size([]))
# print(tree_size([[1, 2, []], 4, [[], 5, 6]]))

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




def contains_key(key, tree):
    # print(tree)
    def inner_node_func(tree, left, right):

        # print('node', tree, 'left', left, 'right', right, 'return',
        # contains_key(left or right, tree), 'left or right', left or right)

        return left or right

    def leaf_func(tree):
        # print('leaf', tree,  tree == key)
        return tree == key

    def empty_tree_func():
        # print('false')
        return False

    return traverse(tree, inner_node_func, leaf_func, empty_tree_func)

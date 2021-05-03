"""
    Test 1 -> write a function that takes in a Binary Tree and return a list of its branch sums ordered from leftmost
    branch to rightmost branch sum
"""

from tree.binarytree import BinaryTree


# branch_sum = []


def get_branch_sum(tree, sum, branch_sum):
    # branch_sum = array

    if tree.left_child:
        sum += tree.left_child.value
        get_branch_sum(tree.left_child, sum, branch_sum)
    branch_sum.append(sum)

    if tree.right_child:
        sum += tree.right_child.value
        get_branch_sum(tree.right_child, sum, branch_sum)

    return branch_sum

# Algo-expert implementation
def branch_sum(root):

    sums = []
    calculate_branch_sum(root, 0, sums)
    return sums


def calculate_branch_sum(node, runningSum, sums):
    if node is None:
        return

    runningSum += node.value
    if node.left_child is None and node.right_child is None:
        sums.append(runningSum)
        return

    calculate_branch_sum(node.left_child, runningSum, sums)
    calculate_branch_sum(node.right_child, runningSum, sums)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)

    left_tree = tree.left_child
    right_tree = tree.right_child

    left_tree.insert_left(4)
    left_tree.insert_right(5)

    left_tree_left = left_tree.left_child
    left_tree_right = left_tree.right_child

    left_tree_left.insert_left(8)
    left_tree_left.insert_right(9)

    left_tree_right.insert_left(10)

    right_tree.insert_left(6)
    right_tree.insert_right(7)

    print(tree.value)
    print(tree.left_child.value)
    print(tree.right_child.value)
    print(left_tree.left_child.value)
    print(left_tree.right_child.value)
    print(right_tree.left_child.value)
    print(right_tree.right_child.value)
    print(left_tree_left.left_child.value)
    print(left_tree_left.right_child.value)
    print(left_tree_right.left_child.value)

    # print(get_branch_sum(tree, tree.value, []))
    print(branch_sum(tree))

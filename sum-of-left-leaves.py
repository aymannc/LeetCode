# Definition for a binary tree node.
"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        if not root: return 0
        some = 0
        q = collections.deque([(0, root)])
        while q:
            type_n, head = q.popleft()
            if type_n and head.left is None and head.right is None:
                some += head.val
            else:
                if head.left is not None:
                    q.append((1, head.left))
                if head.right is not None:
                    q.append((0, head.right))

        return some


# root = TreeNode(3)
# root.right = TreeNode(20)
# root.right.right = TreeNode(7)
# root.right.left = TreeNode(15)
# root.left = TreeNode(9)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(6)
root.right.left = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().sum_of_left_leaves(root))

# Definition for a binary tree node.

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def rec(t1: TreeNode, t2: TreeNode) -> None:
            if t1 is not None and t2 is not None:
                t1.val += t2.val
                return
            if t1.left is None and t2.left is not None:
                t1.left = t2.left
                return
            if t1.right is None and t2.right is not None:
                t1.right = t2.right
                return

        rec(t1, t2)
        return t1


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
print(Solution().mergeTrees(root))

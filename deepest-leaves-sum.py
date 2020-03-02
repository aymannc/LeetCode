"""
Given a binary tree, return the sum of values of its deepest leaves.

"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepest_leaves_sum(self, root: TreeNode) -> int:
        dic = collections.defaultdict(int)

        def rec(root: TreeNode, level: int) -> int:
            if root is None:
                return
            dic[level] += root.val
            rec(root.right, level + 1)
            rec(root.left, level + 1)

        rec(root, 0)
        return dic[max(dic.keys())]

    def deepest_leaves_sum2(self, root: TreeNode) -> int:
        if not root: return
        prev_level = 0
        cur = 0
        q = collections.deque([(0, root)])

        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
            if prev_level == level:
                cur += node.val
            else:
                prev_level = level
                cur = node.val
        return cur


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().deepest_leaves_sum2(root))

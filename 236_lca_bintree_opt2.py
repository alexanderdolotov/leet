'''
236. Lowest Common Ancestor of a Binary Tree - Optimized for Python

Same algorithm, but using a nested local function instead of a recursive
method call. Avoids Python's attribute lookup on `self` at every recursion,
which is a meaningful overhead in a hot recursive loop.

Time: O(n)  Space: O(h) call stack, h = tree height
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        def dfs(node):
            if not node or node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right

        return dfs(root)

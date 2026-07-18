'''
236. Lowest Common Ancestor of a Binary Tree - Optimal Solution

Key insight: the problem guarantees both p and q exist in the tree,
so we don't need to separately track whether each was found.
If a recursive call returns non-None, it found p, q, or their LCA.

If left and right both return non-None, the current node splits them → it's the LCA.
Otherwise bubble up whichever side found something.

Time: O(n)  Space: O(h) call stack, h = tree height
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right

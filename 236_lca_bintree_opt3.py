'''
236. Lowest Common Ancestor of a Binary Tree - Iterative

Avoids Python recursion overhead entirely.

1. DFS with an explicit stack, recording each node's parent.
   Stop as soon as both p and q have been recorded.
2. Walk up from p, adding every ancestor to a set.
3. Walk up from q until we hit a node already in that set → LCA.

Time: O(n)  Space: O(n)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        parent = {root: None}
        stack = [root]

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q
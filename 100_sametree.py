
'''
100. Same Tree
Easy
Topics
premium lock iconCompanies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

 

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # beats 100% run, 75% mem

    def check_same_tree_r(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True 

        if not p:
            return False 

        if not q:
            return False 

        if p.val != q.val:
            return False 

        is_left_true = self.check_same_tree_r(p.left, q.left)
        if not is_left_true:
            return False 

        is_right_true = self.check_same_tree_r(p.right, q.right)
        if not is_right_true:
            return False

        return True



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.check_same_tree_r(p,q) 








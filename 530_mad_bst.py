'''
530. Minimum Absolute Difference in BST
Easy
Topics
premium lock iconCompanies

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 104].
    0 <= Node.val <= 105

 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
 

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root
        # push left spine to reach smallest node first
        while node:
            stack.append(node)
            node = node.left

        prev = None
        min_diff = 10**5 + 1  # values bounded by constraints [0, 10^5]

        while stack:
            node = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            # descend into right child's left spine for next in-order successor
            node = node.right
            while node:
                stack.append(node)
                node = node.left

        return min_diff



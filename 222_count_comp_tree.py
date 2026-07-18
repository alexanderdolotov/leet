

'''

222. Count Complete Tree Nodes
Easy
Topics
premium lock iconCompanies

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [0, 5 * 104].
    0 <= Node.val <= 5 * 104
    The tree is guaranteed to be complete.


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # can run in log n.... 
        # first go left most to identify num of levels. 

        if not root:
            return 0


        num_levels = 1 
        node = root.left 
        while node:
            num_levels += 1
            node = node.left 

        #print(num_levels)


        # go all the way to the right to check if complete.... 

        node = root.right 
        last_level = 1
        while node:
            last_level += 1
            node = node.right 


        if num_levels == last_level: # tree is complete binary tree
            return 2 ** num_levels -1
        
        # now if tree is not complete... run down the middle and check if complete or not.
        # if not complete, go left middle, if complete, go right middle.
        # doing a logn search essentially.   


        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


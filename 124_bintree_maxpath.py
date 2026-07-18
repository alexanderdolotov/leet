
'''
124. Binary Tree Maximum Path Sum
Hard
Topics
premium lock iconCompanies

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

 

Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000

 

Runtime
3ms
Beats99.79%
Memory
23.74MB
Beats90.34%


'''





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    best_ever_sum = 0

    def evaluate_node(self, node:TreeNode) -> int:

        nval = node.val 

        if nval > self.best_ever_sum:
            self.best_ever_sum = nval
        
        best_left = 0 
        best_right = 0

        if node.left:
            best_left = self.evaluate_node(node.left)
            if best_left > self.best_ever_sum:
                self.best_ever_sum = best_left

        if node.right:
            best_right = self.evaluate_node(node.right)
            if best_right > self.best_ever_sum:
                self.best_ever_sum = best_right


        best_sum = nval 
        if best_left > 0 and best_left > best_right:
            best_sum += best_left

        elif best_right > 0 and best_right > best_left:
            best_sum += best_right


        if best_sum > self.best_ever_sum:
            self.best_ever_sum = best_sum

        if best_right + best_left + nval > self.best_ever_sum:
            self.best_ever_sum = best_right + best_left + nval 

       
        return best_sum





    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root:

            if not root.right and not root.left:
                return root.val

            self.best_ever_sum = root.val

            best_sum = self.evaluate_node(root)
            if best_sum > self.best_ever_sum:
                self.best_ever_sum = best_sum

            return self.best_ever_sum
        
        else:
            return 0 

    

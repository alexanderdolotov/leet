'''
637. Average of Levels in Binary Tree
Easy
Topics
premium lock iconCompanies
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

 

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    bin_tree_level_nodes = [[]] # keep track of rolling sum per level, and num of nodes...

    def _descend_tree(self, node, level=0):

        current_level = level+1 
        if current_level >= len(self.bin_tree_level_nodes):
            self.bin_tree_level_nodes.append([0,0]) # new level append

        if node.left: # start from the left
            self.bin_tree_level_nodes[current_level][0] += node.left.val
            self.bin_tree_level_nodes[current_level][1] += 1

            # descend down further on the left... 
            self._descend_tree(node.left, level=current_level)

        if node.right:
            self.bin_tree_level_nodes[current_level][0] += node.right.val
            self.bin_tree_level_nodes[current_level][1] += 1

            # descend down further on the left... 
            self._descend_tree(node.right, level=current_level)



    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []
        
        self.bin_tree_level_nodes = [
            [root.val, 1] # zero level
            ] 

        self._descend_tree(root)

        # get averages at each level
        avgs = []
        for t in self.bin_tree_level_nodes:
            if len(t) == 2 and t[1] > 0:
                avgs.append(t[0] / t[1])


        return avgs





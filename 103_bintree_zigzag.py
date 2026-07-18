'''
103. Binary Tree Zigzag Level Order Traversal
Medium
Topics
premium lock iconCompanies

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

 
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    bin_tree_level_nodes = [[]]

    def _descend_tree(self, node, level=0):

        if not (node.left or node.right):
            return

        current_level = level+1 
        if current_level >= len(self.bin_tree_level_nodes):
            self.bin_tree_level_nodes.append([]) # new level append

        if node.left: # start from the left

            self.bin_tree_level_nodes[current_level].append(node.left.val) # appended left most 

            # descend down further on the left... 
            self._descend_tree(node.left, level=current_level)

        if node.right:
            self.bin_tree_level_nodes[current_level].append(node.right.val) # appended left most 

            # descend down further on the left... 
            self._descend_tree(node.right, level=current_level)



    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
         
        # build out all the nodes at each level, and select rightmost.... 
        if not root:
            return []
        
        self.bin_tree_level_nodes = [
            [root.val] # zero level
            ] 
        
        self._descend_tree(root, level=0)

        for i in range(0, len(self.bin_tree_level_nodes)):

            if i % 2 > 0:
                # run in place list reverse
                level = self.bin_tree_level_nodes[i]
                level.reverse()


        return self.bin_tree_level_nodes





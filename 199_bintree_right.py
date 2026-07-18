'''
199. Binary Tree Right Side View
Medium
Topics
premium lock iconCompanies

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
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




    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # build out all the nodes at each level, and select rightmost.... 
        if not root:
            return []
        
        self.bin_tree_level_nodes = [
            [root.val] # zero level
            ] 
        
        self._descend_tree(root, level=0)

        # build right most list
        result = []
        for i in range(0, len(self.bin_tree_level_nodes)):
            level = self.bin_tree_level_nodes[i]
            if len(level) > 0:
                result.append(level[-1])


        return result




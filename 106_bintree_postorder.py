
from typing import List, Optional

'''

106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

 

Constraints:

    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.

 

'''


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:


    def buildTree_On2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        ilen = len(inorder)
        plen = len(postorder)

        if ilen != plen:
            raise Exception('error error abort!')
        
        if ilen == 0:
            return None 
        
        root_val = postorder[-1]
        
        
        if ilen == 1:
            return  TreeNode(val=root_val) 
        else:
            # find root val in inorder 
            inidx = inorder.index(root_val) # index of rootval 

            # all values on right are right subtree, and left are left subtree
            left_inorder = inorder[0:inidx]
            right_inorder = inorder[inidx+1:]

            left_postorder = postorder[0:inidx]
            right_postorder = postorder[inidx:-1]

            left_tree = self.buildTree_On2(inorder=left_inorder, postorder=left_postorder)
            right_tree = self.buildTree_On2(inorder=right_inorder, postorder=right_postorder)

            return TreeNode(val=root_val, left=left_tree, right=right_tree)

    def buildTree_On(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = [len(postorder) - 1]

        def helper(left, right):
            if left > right:
                return None
            root_val = postorder[post_idx[0]]
            post_idx[0] -= 1
            node = TreeNode(root_val)
            inidx = inorder_map[root_val]
            # right before left: postorder right-to-left is root, right, left
            node.right = helper(inidx + 1, right)
            node.left = helper(left, inidx - 1)
            return node

        return helper(0, len(inorder) - 1)
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree_On(inorder=inorder, postorder=postorder)


sol = Solution()
t = sol.buildTree(inorder=[9,3,15,20,7], postorder=[9,15,7,20,3])
print(t)

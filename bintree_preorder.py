
'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
premium lock iconCompanies

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 

Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.



'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None 

        rootval = preorder[0]
        if len(preorder) == 1:
            return TreeNode(rootval)

        elif len(preorder) == 2:
            if rootval == inorder[0]:  # root first in inorder → only right child
                return TreeNode(rootval, right=TreeNode(preorder[1]))
            else:
                return TreeNode(rootval, left=TreeNode(preorder[1]))
        
        else:
            
            inidx = inorder.index(rootval)
            # check if there is data to left... 
            left_node = None
            right_node = None

            if inidx > 0:
                left_node = self.buildTree(preorder=preorder[1:1+inidx], inorder=inorder[:inidx])

                if inidx < len(inorder) - 1:
                    right_node = self.buildTree(preorder=preorder[1+inidx:], inorder=inorder[inidx+1:])

            else:
                if inidx < len(inorder) - 1:
                    right_node = self.buildTree(preorder=preorder[1:], inorder=inorder[1:]) 

            return TreeNode(rootval, left=left_node, right=right_node)









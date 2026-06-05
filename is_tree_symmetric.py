'''
101. Symmetric Tree
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
 


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # beats 100%

    def check_symmetry(self, lnode, rnode):

        if lnode and rnode:
            if lnode.val == rnode.val: 

                opp1 = self.check_symmetry(lnode.left, rnode.right)
                opp2 = self.check_symmetry(lnode.right, rnode.left)

                return opp1 and opp2

            else:
                return False


        elif not lnode and not rnode:
            return True
        else:
            return False



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root:

            lnode = root.left 
            rnode = root.right 

            if lnode and rnode:
                if lnode.val == rnode.val:

                    opp1 = self.check_symmetry(lnode.left, rnode.right)
                    opp2 = self.check_symmetry(lnode.right, rnode.left)

                    return opp1 and opp2

                else:
                    return False 

            elif not lnode and not rnode:
                return True 
            else:
                return False

        else:
            return True

        
       






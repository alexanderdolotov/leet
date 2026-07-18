'''
108. Convert Sorted Array to Binary Search Tree
Easy
Topics
premium lock iconCompanies

Given an integer array nums where the elements are sorted in ascending order, convert it to a binary search tree.

 

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.

 

'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST_A1(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Runtime
        2ms
        Beats58.64%
        Memory
        20.14MB
        Beats92.71%

                
        '''
        
        # trivial cases 
        if len(nums) == 0: return None 
        if len(nums) == 1: return TreeNode(val=nums[0])
        if len(nums) == 2: return TreeNode(val=nums[0], right=TreeNode(nums[1]))
        if len(nums) == 3: return TreeNode(val=nums[1], left=TreeNode(nums[0]), right=TreeNode(nums[2]))

        # find mid node and recurse down
        mid_idx = len(nums) // 2
        root = TreeNode(val=nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[0:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])

        return root


    def sortedArrayToBST_A2(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Runtime
        3ms
        Beats50.36%
        Memory
        20.39MB
        Beats28.69%
        '''

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(val=nums[mid])
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(nums) - 1)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBST_A1(nums)
    

    
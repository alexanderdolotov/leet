'''
74. Search a 2D Matrix
Medium
Topics
premium lock iconCompanies

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

 


'''


from typing import List

class Solution:

    def mval(self, idx, matrix):

        n = len(matrix[0])
        row = idx // n
        col = idx % n # the remainder

        return matrix[row][col]


    def bin_search(self, sortednums, target, start_idx, end_idx)->bool:

        # basic binary search 

        if start_idx < 0 or end_idx >= len(sortednums) or start_idx > end_idx: return False

        # midpoint:
        mid_idx = (end_idx-start_idx) // 2 + start_idx 
        val = sortednums[mid_idx]

        if target == val: return True

        if target < val: return self.bin_search(sortednums, target, start_idx, mid_idx-1)
        else: return self.bin_search(sortednums, target, mid_idx+1, end_idx)


    def m_search(self, matrix, mn, target, start_idx, end_idx)->bool:

        # basic binary search 

        if start_idx < 0 or end_idx >= mn or start_idx > end_idx: return False

        # midpoint:
        mid_idx = (end_idx-start_idx) // 2 + start_idx 
        val = self.mval(mid_idx, matrix)

        if target == val: return True

        if target < val: return self.m_search(matrix, mn, target, start_idx, mid_idx-1)
        else: return self.m_search(matrix, mn, target, mid_idx+1, end_idx)




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.52MB
        Beats38.22%
        '''

        # this is just binary search, matrix can just be rolled out into vector abstractly using idx function
        mn = len(matrix)*len(matrix[0])

        return self.m_search(matrix, mn, target, 0, mn-1)
    


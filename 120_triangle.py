'''
120. Triangle
Medium
Topics
premium lock iconCompanies

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

 

Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104

 
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
 
'''

from typing import List

class Solution:

    mem = {} # level, insert dict rank

    def triangle_rec(self, triangle: List[List[int]], clevel=0, crow=0) -> int:

        '''
        Runtime
        11ms
        Beats13.25%
        Memory
        21.14MB
        Beats11.20%
        '''

        if clevel == len(triangle)-1: return triangle[clevel][crow] 

        if clevel in self.mem and crow in self.mem[clevel]: return self.mem[clevel][crow] # return precomputed min 

        # compute min left 
        min_left = self.triangle_rec(triangle, clevel+1, crow)

        min_right = self.triangle_rec(triangle, clevel+1, crow+1) 

        min_val = triangle[clevel][crow] + min(min_left, min_right)

        if clevel in self.mem: self.mem[clevel][crow] = min_val 
        else: self.mem[clevel] = {crow: min_val }

        return min_val


    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #self.mem = {}

        #return self.triangle_rec(triangle, 0, 0)
        return self.minimumTotal_iterative(triangle)


    def minimumTotal_iterative(self, triangle: List[List[int]]) -> int:

        # Bottom-up DP: dp[row] holds the min path sum from the current
        # level's `row` cell down to the bottom of the triangle. We start
        # dp as a copy of the last row (each cell's own value, since a
        # path starting there has nowhere left to go), then walk upward
        # collapsing dp into the row above it, one level at a time.
        #
        # At each level, cell `row` can only step down to `row` or `row+1`
        # on the level below, so its best path is its own value plus the
        # cheaper of those two already-computed sums:
        #     dp[row] = triangle[level][row] + min(dp[row], dp[row + 1])
        #
        # dp is reused in place (no dict, no per-cell recursion), so this
        # runs in O(n) extra space where n is the number of rows.
        #
        # Example: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        #   dp starts as the bottom row:      dp = [4, 1, 8, 3]
        #   level 2 (row [6,5,7]):
        #     dp[0] = 6 + min(4,1) = 7
        #     dp[1] = 5 + min(1,8) = 6
        #     dp[2] = 7 + min(8,3) = 10        dp = [7, 6, 10, 3]
        #   level 1 (row [3,4]):
        #     dp[0] = 3 + min(7,6) = 9
        #     dp[1] = 4 + min(6,10) = 10        dp = [9, 10, 10, 3]
        #   level 0 (row [2]):
        #     dp[0] = 2 + min(9,10) = 11        dp = [11, 10, 10, 3]
        #   dp[0] == 11, matching the expected output.

        '''
        Runtime
        4ms
        Beats36.34%
        Memory
        20.01MB
        Beats60.39%

        '''

        n = len(triangle)

        dp = list(triangle[n - 1]) # start from the bottom row

        for level in range(n - 2, -1, -1):

            for row in range(len(triangle[level])):

                dp[row] = triangle[level][row] + min(dp[row], dp[row + 1])

        return dp[0]


'''
64. Minimum Path Sum
Medium
Topics
premium lock iconCompanies

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200

 


'''


from typing import List 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        '''
        Runtime
        7ms
        Beats93.34%
        Memory
        21.45MB
        Beats69.55%

        '''

        # grid[r][c] is turned into the min path sum to reach (r, c),
        # reusing the input as the DP table (no extra space needed).
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue  # starting cell, cost is just itself
                elif r == 0:
                    # top row: only reachable by moving right
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    # left column: only reachable by moving down
                    grid[r][c] += grid[r - 1][c]
                else:
                    # elsewhere: cheapest of arriving from above or from the left
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[rows - 1][cols - 1]





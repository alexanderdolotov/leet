'''
63. Unique Paths II
Medium
Topics
premium lock iconCompanies
Hint

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

 

Constraints:

    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.


'''

from typing import List, Optional

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        '''
        Runtime
        3ms
        Beats21.66%
        Memory
        19.61MB
        Beats10.98%
        '''

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp: List[List[Optional[int]]] = [[None] * n for _ in range(m)]

        def paths_rec(row: int, col: int) -> int:

            if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
                return 0

            if row == 0 and col == 0:
                return 1

            cached = dp[row][col]
            if cached is not None:
                return cached

            paths = paths_rec(row - 1, col) + paths_rec(row, col - 1)
            dp[row][col] = paths

            return paths

        return paths_rec(m - 1, n - 1)
    
    
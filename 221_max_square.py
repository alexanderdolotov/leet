'''
221. Maximal Square
Medium
Topics
premium lock iconCompanies

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.



'''

from typing import List
from collections import deque

class Solution:



    def sol_n3(self, matrix: List[List[str]]) -> int:

        # sanity check... count all 1s and zeros....
        ones = 0
        zeros = 0
        for row in matrix:
            for val in row:
                if val == "1":
                    ones += 1
                else:
                    zeros += 1
        #print(f"ones={ones} zeros={zeros} total={ones + zeros}")

        if ones == 0: return 0
        if ones < 4: return 1
        if zeros == 0: return len(matrix) * len(matrix[0]) # entire matrix is 1s

        # we can check for subsquares of squares for each square visited... 

        visited_squares = {}

        def _check_square_borders(self, matrix, mem, a1, a2, b1, b2) -> int:


            return 1
        

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):


                # check every square... then expand out to largest found square 

                # check for all neighbors: upper right, upper left, lower right, lower left, unless already in visited_squares
                # if all neighbors are 1s, then this is a 3x3 square = 9... 

                # then from each found square... keep expanding out and check all the borders of all the squares to see how far out it can expand... 

                # main issue is overlapping larger square with smaller square... so this sort of forces us to check all squares in n^2 + fan out... 

                pass

        return 1


    def sol_dp_topdown(self, matrix: List[List[str]]) -> int:

        # same shape as the word1/word2 edit-distance top-down: recurse on
        # (i, j), memoize, combine the three neighbor subproblems.

        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}

        def side(i, j) -> int:

            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if matrix[i][j] == "0":
                memo[(i, j)] = 0
                return 0

            up = side(i - 1, j)
            left = side(i, j - 1)
            diag = side(i - 1, j - 1)

            memo[(i, j)] = 1 + min(up, left, diag)
            return memo[(i, j)]

        best = 0
        for i in range(rows):
            for j in range(cols):
                best = max(best, side(i, j))

        return best * best


    def sol_rolling_window(self, matrix):

        '''
        Runtime
        6534ms
        Beats5.02%
        Memory
        32.65MB
        Beats85.53%

        '''
        
        rows = len(matrix)
        cols = len(matrix[0])

        window_size = min(rows, cols)

        while window_size > 0:

            found_square = False

            # col_sum[c] = sum of column c over the current window_size-row band
            col_sum = [0] * cols
            for c in range(cols):
                for r in range(window_size):
                    col_sum[c] += int(matrix[r][c])

            for top in range(rows - window_size + 1):

                if top > 0:
                    # roll the row band down by one: drop the row that left, add the row that entered
                    for c in range(cols):
                        col_sum[c] -= int(matrix[top - 1][c])
                        col_sum[c] += int(matrix[top + window_size - 1][c])

                # col_sum[c] == window_size means column c is all-1s across this row band.
                # scan left to right and track a run of such columns -- the moment we hit
                # a column with a zero in it, every window covering that column is dead,
                # so reset the run instead of checking those windows one by one.
                run_length = 0
                for c in range(cols):
                    if col_sum[c] == window_size:
                        run_length += 1
                        if run_length == window_size:
                            found_square = True
                            break
                    else:
                        run_length = 0

                if found_square:
                    break

            if found_square: return window_size ** 2

            window_size -= 1

        return 1 # should never return 0, because of precounting done earlier...


    def sol_column_fifo(self, matrix):

        '''
        Runtime
        7282ms
        Beats5.02%
        Memory
        32.82MB
        Beats79.94%

        '''

        rows = len(matrix)
        cols = len(matrix[0])

        window_size = min(rows, cols)

        while window_size > 0:

            found_square = False

            for top in range(rows - window_size + 1):

                good_cols = deque() # fifo of the current run of consecutive all-1s columns

                for c in range(cols):

                    if cols - c < window_size - len(good_cols):
                        break # not enough columns left to complete a window_size run

                    is_good = True
                    for r in range(top, top + window_size):
                        if matrix[r][c] == "0":
                            is_good = False
                            break # this column is dead for this band, stop checking its rows

                    if is_good:
                        good_cols.append(c)
                        if len(good_cols) == window_size:
                            found_square = True
                            break
                    else:
                        good_cols.clear() # drop the whole run, next window starts fresh at c + 1

                if found_square:
                    break

            if found_square: return window_size ** 2

            window_size -= 1

        return 1 # should never return 0, because of precounting done earlier...


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # sanity check... count all 1s and zeros....
        ones = 0
        zeros = 0
        for row in matrix:
            for val in row:
                if val == "1":
                    ones += 1
                else:
                    zeros += 1
        #print(f"ones={ones} zeros={zeros} total={ones + zeros}")

        if ones == 0: return 0
        if ones < 4: return 1
        if zeros == 0: return min(len(matrix) , len(matrix[0]))**2 # entire matrix is 1s




        return self.sol_column_fifo(matrix)
    

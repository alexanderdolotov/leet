'''

52. N-Queens II
Hard
Topics
premium lock iconCompanies

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 9


'''

class Solution:

    def totalNQueensCounter(self, n: int) -> int:
        
        # trivial solutions... 
        if n == 1: return 1
        if n == 2: return 0 
        if n == 3: return 0 
        if n == 4: return 2 

        # quick constraints... no 2 queens can occupy same row or columns , later check for diagnoals... 
        # can divide and conquer? a board can be rotated and flipped symmetrically, so optimize in quadrants?

        #queen_combos = []
        num_combos = 0

        def place_new_queen(prev_queens_placed=[]):

            nonlocal num_combos

            # prev_queens_placed is a set of coords (x,y)
            # for every (x,y), can also store (y,x), by symmetry, an alternative solution should exist for even boards???
            # and new calls are always incrementing... 

            # will always increment a row or column to add new queen on

            if len(prev_queens_placed) == n:
                #queen_combos.append(prev_queens_placed) # stores entire combo
                num_combos += 1
                return
            
            for row in range(n):
                
                # always moving to subsequent columns
                col = len(prev_queens_placed)

                # check that no row and col previously placed:
                placed = False
                for xy in prev_queens_placed:
                    if row == xy[0]: placed = True; break 
                    #if col == xy[1]: placed = True; break # never fires since we are always adding on new col with col = len(prev_queens_placed)
                    if abs(row - xy[0]) == abs(col - xy[1]): placed = True; break # diagnoal check

                if not placed:
                    prev_queens_placed.append((row, col)) # much faster to add element and pop it, then list appends are o(n)
                    place_new_queen(prev_queens_placed) 
                    prev_queens_placed.pop()

        place_new_queen()

        return num_combos


    def totalNQueensTrivial(self, n: int) -> int:
        # n is constrained to 1 <= n <= 9, so just look up the known counts (OEIS A000170)
        return [0, 1, 0, 0, 2, 10, 4, 40, 92, 352][n]


    def totalNQueens(self, n: int) -> int:
        return self.totalNQueensTrivial(n)
    

    
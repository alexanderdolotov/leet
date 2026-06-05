from typing import List

'''
289. Game of Life
Medium
Topics
premium lock iconCompanies

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

'''

class Solution:
    # beats 100% performance. Beats 58% nemory

    def count_live_neighs(self, board, row, col, nrows, ncols):

        live = 0

        # check if on edge of board. assumes board is >= 2x2. 

        if row == 0:
            if col == 0: # top left corner:
                live += board[row+1][col]
                live += board[row][col+1]
                live += board[row+1][col+1]
                return live
            elif col == ncols - 1: # top right corner 
                live += board[row+1][col]
                live += board[row][col-1]
                live += board[row+1][col-1]
                return live
            else:
                # top row, not corner
                
                live += board[row][col+1]
                live += board[row][col-1]

                live += board[row+1][col]
                live += board[row+1][col+1]
                live += board[row+1][col-1]
                return live


        elif row == nrows - 1:
            if col == 0: # bottom left corner:
                live += board[row-1][col]
                live += board[row][col+1]
                live += board[row-1][col+1]
                return live
            elif col == ncols - 1: # bottom right corner 
                live += board[row-1][col]
                live += board[row][col-1]
                live += board[row-1][col-1]
                return live
            else:
                # bottom row not corner
                live += board[row][col+1]
                live += board[row][col-1]

                live += board[row-1][col]
                live += board[row-1][col+1]
                live += board[row-1][col-1]
                return live


        if col == 0:
            # left col, not corner
            live += board[row-1][col]
            live += board[row+1][col]

            live += board[row][col+1]
            live += board[row-1][col+1]
            live += board[row+1][col+1]
            return live 

        elif col == ncols - 1:
            # right col, not corner 
            live += board[row-1][col]
            live += board[row+1][col]

            live += board[row][col-1]
            live += board[row-1][col-1]
            live += board[row+1][col-1]
            return live 

        # middle case 
        live += board[row-1][col]
        live += board[row+1][col]

        live += board[row][col-1]
        live += board[row-1][col-1]
        live += board[row+1][col-1]

        live += board[row][col+1]
        live += board[row-1][col+1]
        live += board[row+1][col+1]
 
        return live


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        nrows = len(board)
        if nrows == 0:
            return
       
        ncols = len(board[0])

        if nrows <= 1 and ncols <= 1:
            board[0][0] = 0
            return 


        cell_flips = []
        if nrows == 1:
            # find cells to keep alive
            for col in range(0, ncols):
                cell = board[0][col]
                if col == 0 and cell == 1:
                    cell_flips.append((0,0))
                elif col == ncols - 1 and cell == 1:
                    cell_flips.append((0,ncols - 1))
                else:
                    if cell == 1 and ( board[0][col-1] == 0 or board[0][col+1] == 0 ):
                        cell_flips.append((0,col))

            for cell in cell_flips:
                board[cell[0]][cell[1]] = 0

            return



        if ncols == 1:
            # find cells to keep alive
            for row in range(0, nrows):
                cell = board[row][0]
                if row == 0 and cell == 1:
                    cell_flips.append((0,0))
                elif row == nrows - 1 and cell == 1:
                    cell_flips.append((nrows - 1,0))
                else:
                    if cell == 1 and ( board[row-1][0] == 0 or board[row+1][0] == 0 ):
                        cell_flips.append((row,0))

            for cell in cell_flips:
                board[cell[0]][cell[1]] = 0
                
            return


        for row in range(0, nrows):
            for col in range(0, ncols):
                curent_state = board[row][col]
                live_neighs = self.count_live_neighs(board, row, col, nrows, ncols)

                # rules of life
                if curent_state == 1:
                    if live_neighs < 2:
                        cell_flips.append((row,col))
                    elif live_neighs > 3:
                        cell_flips.append((row,col)) 

                else:
                    if live_neighs == 3:
                        cell_flips.append((row,col)) 

    

        for cf in cell_flips:
            cell = board[cf[0]][cf[1]]
            board[cf[0]][cf[1]] = 1 - cell

        


s = Solution()

#board = [[1,1,0,1,1,1]]
#board =  [[1],[1],[0],[1],[1],[1]]
#board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]

out = s.gameOfLife(board)

print(board)




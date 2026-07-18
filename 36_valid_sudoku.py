from typing import List


'''
36. Valid Sudoku
Medium
Topics
premium lock iconCompanies

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

'''


class Solution:

    VALID_CHARS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


    def valid_rows(self, board: List[List[str]]) -> bool:

        
        for i in range(0,9):
            row = board[i]
            chars_count = set()
            for c in row:
                if c == '.':
                    continue 

                if c not in self.VALID_CHARS:
                    return False 
                
                if c in chars_count:
                    return False 

                chars_count.add(c)
                

        return True 


    def valid_cols(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            chars_count = set()
            for j in  range(0,9):
                c = board[j][i]
                if c == '.':
                    continue

                if c not in self.VALID_CHARS:
                    return False 
                
                if c in chars_count:
                    return False 

                chars_count.add(c)
            

        return True 


    def valid_3x3(self, board: List[List[str]]) -> bool:


        for i in range(0, 9, 3):
            
            for j in  range(0, 9, 3):
                chars_count = set()
                for i2 in range(i, i+3, 1):
                    for j2 in range(j, j+3, 1):
                        c = board[i2][j2]
                        if c == '.':
                            continue

                        if c not in self.VALID_CHARS:
                            return False 
                        
                        if c in chars_count:
                            return False 

                        chars_count.add(c)


        return True 


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows_are_valid = self.valid_rows(board=board)
        if not rows_are_valid:
            return False 

        cols_are_valid = self.valid_cols(board=board)

        if not cols_are_valid:
            return False 

        
        return self.valid_3x3(board=board)



s = Solution()
out = s.isValidSudoku(board=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(out)
     



from typing import List


'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

'''


class Solution:


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        nrows = len(matrix)
        if nrows == 0:
            return
       
        ncols = len(matrix[0])

        if nrows <= 1 and ncols <= 1:
            return 

        
        # just keep track of zeroed cols
        zero_cols = []
        found_zero = False
        for row in range(0, nrows):

            found_zero = False
            for col in range(0, ncols):

                val = matrix[row][col] 
                
                if val == 0:
                    # add col to zeroed col
                    zero_cols.append(col)
                    found_zero = True

            if found_zero:     
                # set all row to zero and continue to next row. 
                for zrow in range(0, ncols):
                    matrix[row][zrow] = 0

        if found_zero:     
            # set all row to zero and continue to next row. 
            for zrow in range(0, ncols):
                matrix[nrows-1][zrow] = 0


        for zcol in zero_cols:
            for row in range(0,nrows):
                matrix[row][zcol] = 0





s = Solution()

matrix = [[0,1]]

out = s.setZeroes(matrix)

print(matrix)



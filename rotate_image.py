from typing import List


'''

48. Rotate Image
Medium
Topics
premium lock iconCompanies

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000


'''

class Solution:

    def swap(self, matrix, r1, c1, r2, c2):

        temp = matrix[r1][c1]
        matrix[r1][c1] = matrix[r2][c2]
        matrix[r2][c2] = temp


    def four_way_swap(self, matrix, r1, c1, n):

        self.swap(matrix, r1, c1, n-1-c1, r1)
        #print(matrix)
        self.swap(matrix, n-1-c1, r1, n-1-r1, n-1-c1)
        #print(matrix)
        self.swap(matrix, n-1-r1, n-1-c1, c1, n-1-r1)
        #print(matrix)



    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        nrows = len(matrix)
        if nrows <= 1:
            return 

        ncols = len(matrix[0])
        
        if ncols <= 1:
            return

        if ncols != nrows:
            raise Exception('error. error.')


        a = 0
        b = nrows-1
        i = 0
        while a < b:

            for x in range(a, b):
                #print(x, matrix)
                self.four_way_swap(matrix, i, x, nrows)
                #input()

            a += 1
            b -= 1
            i += 1
            
        
        return 





s = Solution()

matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
    ]

out = s.rotate(matrix)

print(matrix)

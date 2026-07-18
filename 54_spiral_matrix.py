from typing import List


'''
54. Spiral Matrix
Medium
Topics
premium lock iconCompanies
Hint

Given an m x n matrix, return all elements of the matrix in spiral order.

 


Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

 

'''


class Solution:

    LIMIT = 101

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        nrows = len(matrix)

        # result for 1xN matrix
        if nrows == 1:
            return matrix[0]

        # result for Nx1 matrix
        ncols = len(matrix[0])
        if ncols == 1:
            for i in range(0,nrows):
                result.append(matrix[i][0])

            return result


        result.append(matrix[0][0])
        matrix[0][0] = self.LIMIT

        i = 0
        j = 1 # move one step right
        prev_dir = 0 # 0 right, 1 down, 2 left, 3 up
        while True:
            if matrix[i][j] == self.LIMIT:
                return result

            #print(matrix)

            result.append(matrix[i][j])

            matrix[i][j] = self.LIMIT

            if prev_dir == 0: 
                if j+1 < ncols and matrix[i][j+1] < self.LIMIT: # keep moving right if room
                    j += 1
                else:
                    i += 1 # move down
                    prev_dir = 1 

            elif prev_dir == 1:
                if i + 1 < nrows and matrix[i+1][j] < self.LIMIT: # keep moving down
                    i += 1
                else:
                    j -= 1 # move left 
                    prev_dir = 2 
            elif prev_dir == 2:
                if j - 1 >= 0 and matrix[i][j-1] < self.LIMIT:
                    j -= 1 # keep moving left 
                else:
                    i -= 1
                    prev_dir = 3 
            else:
                if i - 1 >= 0 and matrix[i-1][j] < self.LIMIT:
                    i -= 1 # keep moving up
                else:
                    j += 1 # move right
                    prev_dir = 0



            
            



s = Solution()
out = s.spiralOrder(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    )

print(out)
out = s.spiralOrder([[1], [2], [3]])

print(out)



'''
6. Zigzag Conversion
Medium
Topics
premium lock iconCompanies

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000



'''


class Solution:

    def convert_pretty(self, s: str, numRows: int) -> str:


        SPACE = ' '

        rows = ['']*numRows

        if numRows == 1:
            return s
        

        move_down = True
        row = 0
        for i in range(0, len(s)):
            c = s[i]

            
            if row == 0: 
                move_down = True

            #print(row)
            if move_down:
                rows[row] += c + SPACE*(numRows-row-1)
                if row == 0: 
                    rows[row] += SPACE
            else:
                rows[row] += c + SPACE*(row)

            if move_down:
                row += 1
            
            if row >= numRows:
                move_down = False
                row -= 1 
                rows[row] += SPACE*numRows
            
            if not move_down:

                row -= 1 

            if row < 0:
                move_down = True
                row += 1
                row += 1


        
        finalstr = ''
        for r in rows:
            finalstr += r + '\n'

        print(finalstr)
        finalstr = finalstr.replace(' ', '').replace('\n','')

        return finalstr



    def convert(self, s: str, numRows: int) -> str:
        
        
        rows = ['']*numRows

        if numRows == 1:
            return s
        

        move_down = True
        row = 0
        for i in range(0, len(s)):
            c = s[i]

            if row == 0: 
                move_down = True

            rows[row] += c 

            if move_down:
                row += 1
            
            if row >= numRows:
                move_down = False
                row -= 1 
                
            
            if not move_down:
                row -= 1 

            if row < 0:
                move_down = True
                row += 1
                row += 1


        
        finalstr = ''
        for r in rows:
            finalstr += r 

        return finalstr

    
s = Solution()
out = s.convert('PAYPALISHIRING', 4)
print(out)

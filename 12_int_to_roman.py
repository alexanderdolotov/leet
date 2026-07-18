import math 

'''
12. Integer to Roman
Medium

Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

    If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV

 

Constraints:

    1 <= num <= 3999



'''

class Solution:


    # beats 100%
    def intToRoman(self, num: int) -> str:

        roman_str = ''
        d4 = int(num / 1000)
        d3 = int((num-d4*1000) / 100)
        d2 = int((num-d4*1000-d3*100) / 10)
        d1 = num - d4*1000 - d3*100 - d2*10
        
        print(d4, d3, d2, d1)

        if d4 > 0:
            roman_str += 'M'*d4
        
        if d3 >= 5:
            if d3 == 9:
                roman_str += 'CM'
            else:
                roman_str += 'D'
                roman_str += 'C'*(d3-5)

        else:
            if d3 == 4:
                roman_str += 'CD' 
            else:
                roman_str += 'C'*d3


        if d2 >= 5:
            if d2 == 9:
                roman_str += 'XC'
            else:
                roman_str += 'L'
                roman_str += 'X'*(d2-5)
        else:
            if d2 == 4:
                roman_str += 'XL'
            else:
                roman_str += 'X'*d2

        if d1 >= 5:
            if d1 == 9:
                roman_str += 'IX'
            else:
                roman_str += 'V'
                roman_str += 'I'*(d1-5)
        else:
            if d1 == 4:
                roman_str += 'IV'
            else:
                roman_str += 'I'*d1
        

        return roman_str



s = Solution()
out = s.intToRoman(num=3042)
print(out)


'''
67. Add Binary
Easy
Topics
premium lock iconCompanies

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.



'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # i can loop thru each string from right to left, add parallel numbers, and carry the 1 over if both 1...
        # can end up carrying several 1s over ex. "111" + "111" = "1110"

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # total max can be is 3 
            result.append(str(total % 2)) # if 3, then 1, if 2, then 0, if 1, then 1.
            carry = 1 if total >= 2 else 0 # max can be carried is 1

        return "".join(reversed(result))

'''
22. Generate Parentheses
Medium
Topics
premium lock iconCompanies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

 


'''

from typing import List


class Solution:
    def generateParenthesisStack(self, n: int) -> List[str]:
        

        # another back tracking... for each ( paranthesis, make binary choice: close it or keep going.
        # so total solution should be ~2^n
        # iterate and keep track of open and todo paranethsis, creating a permutation

        results = []
        stack = [('', 0, 0)]  # (current string, open_count, close_count)

        while stack:
            current, open_count, close_count = stack.pop()

            if len(current) == 2 * n:
                results.append(current)
                continue

            if open_count < n:
                stack.append((current + '(', open_count + 1, close_count))
            if close_count < open_count:
                stack.append((current + ')', open_count, close_count + 1))

        return results

    def generateParenthesisRecursive(self, n: int) -> List[str]:
        results = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                results.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return results


    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesisRecursive(n)
    
    
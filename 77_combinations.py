'''
77. Combinations
Medium
Topics
premium lock iconCompanies

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

 

Constraints:

    1 <= n <= 20
    1 <= k <= n

 
'''


class Solution:
    def combine_cross(self, n: int, k: int) -> List[List[int]]: # slowest, sql like
        
        explosion = [[]]

        def cross_product():
            nonlocal explosion
            new_explosion = []
            for combo in explosion:
                start = combo[-1] + 1 if combo else 1
                for d in range(start, n + 1):
                    new_explosion.append(combo + [d])
            explosion = new_explosion

        for _ in range(k):
            cross_product()

        return explosion
    
    def combine_opt(self, n: int, k: int) -> List[List[int]]: # fastest, no recursion. clean loop
        result = []
        combo = list(range(1, k + 1))

        while True:
            result.append(combo.copy())
            
            i = k - 1 # work backwards... 
            while i >= 0 and combo[i] == n - k + 1 + i: 
                i -= 1

            if i < 0:
                break # break loop once all permutations completed

            combo[i] += 1
            for j in range(i + 1, k):
                combo[j] = combo[i] + j - i


        return result


    def combine_backtrack(self, n: int, k: int): # mid performance, recursive.. 
        result = []
        combo = []

        def backtrack(start):
            if len(combo) == k:
                result.append(combo.copy())
                return
            for d in range(start, n + 1):
                combo.append(d)
                backtrack(d + 1)
                combo.pop()

        backtrack(1)
        return result

    def combine(self, n: int, k: int): 
        return self.combine_backtrack(n,k)
    

'''
97. Interleaving String
Medium
Topics
premium lock iconCompanies

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

 

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

 

Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.


'''



class Solution:


    def interleave_recmem(self, s1: str, s2: str, s3: str, i1: int, i2: int, mem: dict) -> bool:
        # s1, s2, s3 are never sliced - i1/i2 are indexes into the ORIGINAL
        # strings, so (i1, i2) unambiguously identifies a subproblem and is
        # safe to use as a memo key across the whole call tree


        '''
        Runtime
        50ms
        Beats63.64%
        Memory
        19.64MB
        Beats37.19%
        '''
        
        if (i1, i2) in mem: return mem[(i1, i2)]

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        start1, start2 = i1, i2

        for i3 in range(i1 + i2, len3):

            c = s3[i3]

            # bounds-check before indexing s1/s2 since i1 or i2 may already equal its length
            s1_in_bounds = i1 < len1
            s2_in_bounds = i2 < len2

            s1_matches = s1_in_bounds and c == s1[i1]
            s2_matches = s2_in_bounds and c == s2[i2]

            # check if char can be leaved from s1 or s2
            if not s1_matches and not s2_matches:
                mem[(start1, start2)] = False
                return False

            if s1_matches and not s2_matches:
                # found leave, increment
                i1 += 1
                continue

            if not s1_matches and s2_matches:
                # found leave, increment
                i2 += 1
                continue

            if s1_matches and s2_matches:
                # now either can be used to interleave... split the algorithm into choice subsections

                s1_results = self.interleave_recmem(s1, s2, s3, i1 + 1, i2, mem)
                if s1_results:
                    mem[(start1, start2)] = True
                    return True

                s2_results = self.interleave_recmem(s1, s2, s3, i1, i2 + 1, mem)

                result = s1_results or s2_results
                mem[(start1, start2)] = result
                return result

        # loop finished without hitting a tie or a mismatch: every char was
        # consumed via a forced single-path match, so it's a valid interleave
        mem[(start1, start2)] = True
        return True


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        return self.interleave_recmem(s1, s2, s3, 0, 0, {})


    def isInterleaveDP(self, s1: str, s2: str, s3: str) -> bool:
        # fixes the TLE above: no memoization meant the tie-branch recursion
        # re-explored the same (i1, i2) state exponentially on repeated chars

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3: return False

        # dp[i][j] = True if the first i chars of s1 and first j chars of s2
        # interleave to form the first i+j chars of s3
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    continue

                k = i + j - 1

                take_from_s1 = i > 0 and dp[i - 1][j] and s1[i - 1] == s3[k]
                take_from_s2 = j > 0 and dp[i][j - 1] and s2[j - 1] == s3[k]

                dp[i][j] = take_from_s1 or take_from_s2

        return dp[len1][len2]


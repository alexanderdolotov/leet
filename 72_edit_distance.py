
'''
72. Edit Distance
Medium
Topics
premium lock iconCompanies

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

 

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.



'''


class Solution:


    def sol1(self, word1: str, word2: str, mem={}, i=0, j=0) -> int:
        
        ''' 
        Runtime
        62ms
        Beats12.71%
        Memory
        19.80MB
        Beats89.47%

        '''

        # levenshtian distance ... 

        # every word can be fully deleted, and inserted as word2... so max operations is bounded by len(word1) + len(word2)
        #upper_bound = len(word1) + len(word2) # this upper bound is too high because we have replace() also here

        upper_bound = max(len(word1) - i, len(word2) - j) # we can just replace all word1 chars with word2 chars, and insert/delete remainder...

        # if words differ in length... least possible operations would be to remove excess characters
        lower_bound = upper_bound - min(len(word1) - i, len(word2) - j)

        if upper_bound == 0: return 0
        if i == len(word1): return len(word2) - j
        if j == len(word2): return len(word1) - i


        # if result has already existed, return cache
        if i in mem and j in mem[i]: return mem[i][j]

        # strategy: ... use replace() and try to keep existing letters to avoid 2 operations: delete/insert ... 
        # now characters that are same and in same order can be kept... to minimize inserts/deletes. 
        # then replace any missing characters in between same and in order ones.... 
        # problem sort of builds on top of longest subsequence DP problem... 

        
        # can always start with naive DP... iter on every character and pick 1 of 3 operations...
        # worst case could be a 3^upper_bound explosion... since for every char... 3 possible operations are being performed... 

        # the idea to keep common letters, and replace mid differing ones, seems to work in ideal, but probably not even in practice...

        # "abcdk" - > "kdabc" ... so, insert k and delete dk is 3 operation... but the heuristic to delete abcd, keep k, and insert is worse... 

        # run sanity check if any letters even match, if not, just return upper bound 
        # set1 = set()
        # set2 = set()

        # for i2 in range(i, len(word1)):
        #     set1.add(word1[i2])

        # for j2 in range(j, len(word2)):
        #     set2.add(word2[j2])
      

        '''
        Runtime
        295ms
        Beats5.09%
        Memory
        22.74MB
        Beats47.36%
        
        '''

        
        # iset = set1.intersection(set2) # common characters between words

        # if len(iset) == 0: return upper_bound # if no same characters exist, return upper bound

        # need to figure out what to do with common characters, as they may be across different indexes and out of sequence...

        # it seems that finding the longest common sequence is the best way to go... although not sure if counter examples can exist??

        # can i leverage the characters indexed in dicts to better find longest running subsequence... ?

        # keep an overlapping set of chars 

        
        c1 = word1[i]
        c2 = word2[j]

        if c1 == c2: mem.setdefault(i, {})[j] = self.sol1(word1, word2, mem, i+1, j+1); return mem[i][j]
            

        # try 3 possible operations

        # replace 
        rops = self.sol1(word1, word2, mem, i+1, j+1) + 1

        # delete
        delops = self.sol1(word1, word2, mem, i+1, j) + 1

        # insert 
        iops = self.sol1(word1, word2, mem, i, j+1) + 1

        minops = min(rops, delops, iops)

        mem.setdefault(i, {})[j] = minops


        return mem[i][j]



    def sol2(self, word1: str, word2: str) -> int:


        '''
        Runtime
        51ms
        Beats47.95%
        Memory
        22.93MB
        Beats28.15%
        '''

        n, m = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[i:] into word2[j:]
        # same meaning as sol1's (i, j) state, just built bottom-up instead of top-down.
        # size (n+1) x (m+1) so index n and index m are valid -- those are the "ran out
        # of characters" base cases (equivalent to sol1's i == len(word1) / j == len(word2))
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case: word2[j:] is empty -> delete every remaining char of word1[i:]
        for i in range(n + 1):
            dp[i][m] = n - i

        # base case: word1[i:] is empty -> insert every remaining char of word2[j:]
        for j in range(m + 1):
            dp[n][j] = m - j

        # fill everything else. dp[i][j] depends on dp[i+1][j+1], dp[i+1][j], dp[i][j+1] --
        # all cells with a larger i or j -- so we must fill those first. that means looping
        # i and j downward from the end, finishing at (0, 0) last.
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if word1[i] == word2[j]:
                    # characters already match: no operation spent here, just inherit
                    # the answer for the rest of both strings
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    replace = dp[i + 1][j + 1] + 1  # swap word1[i] for word2[j], advance both
                    delete = dp[i + 1][j] + 1       # drop word1[i], word2[j] still unmatched
                    insert = dp[i][j + 1] + 1        # insert word2[j] into word1, word1[i] still unmatched

                    dp[i][j] = min(replace, delete, insert)

        # (0, 0) covers the full word1 vs the full word2
        return dp[0][0]



    def sol3(self, word1: str, word2: str) -> int:

        '''
        Runtime
        39ms
        Beats77.51%
        Memory
        19.17MB
        Beats99.30%

        '''

        n, m = len(word1), len(word2)

        # only two rows are ever needed at once: the row for i+1 ("prev") and the
        # row currently being built for i ("curr") -- dp[i][j] never reads from
        # i+2 or beyond, so keeping the full n+1 row table around (like sol2 does)
        # is wasted space. this drops memory from O(n*m) down to O(m).

        # prev starts as dp[n][*]: word1 is fully exhausted, so word2[j:] must all be inserted
        prev = [m - j for j in range(m + 1)]

        for i in range(n - 1, -1, -1):

            # curr will become dp[i][*]. curr[m] is the base case: word2 is exhausted,
            # so the remaining word1[i:] must all be deleted
            curr = [0] * (m + 1)
            curr[m] = n - i

            for j in range(m - 1, -1, -1):

                if word1[i] == word2[j]:
                    curr[j] = prev[j + 1]
                else:
                    replace = prev[j + 1] + 1  # dp[i+1][j+1]
                    delete = prev[j] + 1       # dp[i+1][j]
                    insert = curr[j + 1] + 1   # dp[i][j+1] -- already built earlier in this row

                    curr[j] = min(replace, delete, insert)

            # this row is done -- it becomes "prev" for the next (smaller) i
            prev = curr

        # after i = 0 finishes, prev holds row 0: the full word1 vs the full word2
        return prev[0]



    def minDistance(self, word1: str, word2: str) -> int:


        #return self.sol1(word1, word2, {})
    
        return self.sol3(word1, word2)
    


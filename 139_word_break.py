'''
139. Word Break
Medium

Topics
premium lock icon
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

'''

from typing import List


class Solution:

    word_set = set()
    longest_word_length = 0
    shortest_word_length = 0

    results_found = {} # keeps memory of already found results for substrings so as not to double check them again

    def word_break_rec(self, s: str) -> bool:
        max_i = min(self.longest_word_length, len(s))
        for i in range(max_i, self.shortest_word_length - 1, -1):
            slookup = s[:i]

            if slookup in self.word_set:
                if i == len(s):
                    return True
                
                next_substr = s[i:]
                if next_substr in self.results_found:
                    return self.results_found[next_substr]
                
                substr_result = self.word_break_rec(next_substr)
                if substr_result:
                    self.results_found[next_substr] = True
                    return True
                else:
                    self.results_found[next_substr] = False

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.word_set = set(wordDict)
        lengths = [len(word) for word in wordDict]
        self.longest_word_length = max(lengths)
        self.shortest_word_length = min(lengths)
        self.results_found  = {}

        return self.word_break_rec(s)
    
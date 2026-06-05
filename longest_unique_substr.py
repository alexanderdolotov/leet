from typing import List


'''
3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, find the length of the longest without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

 


'''



class Solution:

    def n2_sol(self, s: str) -> int:

        lens = len(s)
        if lens == 0:
            return 0

        longest_len = 1
        for i in range(lens):
 
            known_chars = set()
            known_chars.add(s[i])

            for j in range(i+1, lens, 1):
                cnext = s[j]

                if cnext in known_chars:
                    break 
                else:
                    known_chars.add(cnext)

            runlen = len(known_chars)
            if runlen > longest_len:
                longest_len = runlen


        return longest_len


    
    def rolling_window_sol(self, s: str) -> int:

        lens = len(s)
        if lens == 0:
            return 0

        longest_len = 1
        char_index = {s[0]: 0}
        i = 1
        while i < lens:
            cnext = s[i]

            if cnext in char_index:
                ilen = len(char_index)
                if ilen > longest_len:
                    longest_len = ilen

                i = char_index[cnext] 
                char_index = {}

            else:
                char_index[cnext] = i


            i += 1

        
        ilen = len(char_index)
        if ilen > longest_len:
            longest_len = ilen

        return longest_len




    def lengthOfLongestSubstring(self, s: str) -> int:
        
        

        return self.rolling_window_sol(s)



s = Solution()
out = s.lengthOfLongestSubstring('abcdddddabcdefghhh')
print(out)
     

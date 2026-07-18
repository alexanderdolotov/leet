
from typing import List


'''

14. Longest Common Prefix
Easy
Topics
premium lock iconCompanies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

 
'''

class Solution:

    def append_word_chars(self, word:str, d):

        running_dict = d 
        for c in word:
            if c not in running_dict:
                newd = {'num': 1}
                running_dict[c] = newd
                running_dict = newd
            else:
                newd = running_dict[c]
                newd['num'] += 1 
                running_dict = newd


    def longestCommonPrefix2(self, strs: List[str]) -> str:
        words = {}
        for word in strs:
            self.append_word_chars(word, words)

        print(words)
        
        max_count = 0
        running_pref = ''
        running_c = ''
        running_dict = words
        run = True
        while run:

            run = False
            print(running_dict.keys())
            for c in running_dict.keys():
                if c == 'num':
                    continue
                if running_dict[c]['num'] >= max_count:
                    max_count = running_dict[c]['num'] 
                    running_c = c 
                    run = True 

            # check if there are ties for max_count:
            ties = 0
            for c in running_dict.keys():
                if c == 'num':
                    continue
                if running_dict[c]['num'] == max_count:
                    ties += 1 

            if ties > 1:
                run=False
                break

            if max_count > 0 and run:
                running_dict = running_dict[running_c]
                running_pref += running_c
            else:
                break

            print(running_c, running_pref)


        

        return running_pref



    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        words = len(strs)
        common_chars = ''

        char_i = 0
        char = ''
        char_count = 0
        while True:
            for word in strs: 
                if len(word) <= char_i:
                    return common_chars
                else:
                    if len(char) == 0:
                        char = word[char_i]
                        char_count += 1 
                    else:
                        if char == word[char_i]:
                            char_count += 1 
                        else:
                            return common_chars 

            if char_count == words:
                common_chars += char 
                char = ''
                char_count = 0 
                char_i += 1
            else:
                return common_chars 
            

        return common_chars

       
    
s = Solution()
out = s.longestCommonPrefix(["flower","flow","flight"])
print(out)



'''
Example trie after ["dog", "racecar", "car"]:

{
    'd': {
        'num': 1,
        'o': {
            'num': 1,
            'g': {'num': 1},
        },
    },
    'r': {
        'num': 1,
        'a': {
            'num': 1,
            'c': {
                'num': 1,
                'e': {
                    'num': 1,
                    'c': {
                        'num': 1,
                        'a': {
                            'num': 1,
                            'r': {'num': 1},
                        },
                    },
                },
            },
        },
    },
    'c': {
        'num': 1,
        'a': {
            'num': 1,
            'r': {'num': 1},
        },
    },
}
'''
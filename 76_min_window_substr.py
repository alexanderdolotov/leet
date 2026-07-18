from typing import List



''' 
76. Minimum Window Substring
Hard
Topics
premium lock iconCompanies
Hint

Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 


'''


class Solution:


    def logN_subarray_search(self, s: str, t: str) -> str:

        
        # Do rolling windows starting at mid size, and decrease / or increase whether sub array found. 
        # O = N * lgN  

        # rolling scan can add/subtract chars in O1 time to rolling dict and keep count of critical chars

        # TODO


        return ''



    def is_subset_dict(self, rd, td):

        for c in td:
            if c not in rd:
                return False 
            if rd[c] < td[c]:
                return False


        return True


    def minWindow(self, s: str, t: str) -> str:
        
        slen = len(s)
        tlen = len(t)

        if slen < tlen:
            return ''


        word_dict = {}
        charsum = 0
        for c in t:
            
            if c in word_dict:
                word_dict[c] += 1 
            else:
                word_dict[c] = 1

            charsum += ord(c)

        
        #print('charsum', charsum)
        #print('word_dict', word_dict)

        # find char indexes 
        char_indexes = {}

        # one linear scan to get indexes of all critical chars
        key_indexes = []
        for i in range(0, slen):
            c = s[i]
            if c in word_dict:
                key_indexes.append(i)
                # may not need an array, just keep count
                # if c in char_indexes:
                #     char_indexes[c].append(i)
                # else:
                #     char_indexes[c] = [i]

                if c in char_indexes:
                    char_indexes[c] += 1
                else:
                    char_indexes[c] = 1



        #print('key_indexes', key_indexes)
        #print('char_indexes', char_indexes)

        # check if all chars are there
        for c in word_dict.keys():
            if c not in char_indexes:
                return ''

            if (char_indexes[c]) < word_dict[c]:
                return ''


        # if all key chars are present, and stirng are equal, therefor is a permutaiton
        if tlen == slen:
            return s


        # iterate through critical indexes
        running_len = tlen 
        
        i = 0
        running_dict = {}
        # initialize dict 

        i = 0
        ki = 0
        for i in range(0,running_len):
            ki = key_indexes[i]
            c = s[ki]
            if c in running_dict:
                running_dict[c] += 1 
            else:
                running_dict[c] = 1 


        #print('running_dict', running_dict)
        shortest_window = ()
        shortest_running_len = slen
        is_subset = self.is_subset_dict(running_dict, word_dict)
        if is_subset:
            
            kj =  key_indexes[running_len-1]
            ki =  key_indexes[0]

            shortest_running_len = kj - ki + 1

            shortest_window = (0,running_len-1)
            if shortest_running_len == tlen:

                return s[key_indexes[shortest_window[0]]:key_indexes[shortest_window[1]]+1]
            
        

        #print('shortest_running_len', shortest_running_len, 'shortest_window', shortest_window)

        j = running_len - 1
        i = 0
        

        while j < slen and j < len(key_indexes)-1:
            #print(i, j)

            j += 1
            kj = key_indexes[j]
            ki = key_indexes[i]
            c = s[kj]

            if c in running_dict:
                running_dict[c] += 1 
            else:
                running_dict[c] = 1 

            #print(running_dict)

            is_subset = self.is_subset_dict(running_dict, word_dict)
            if is_subset:
                newlen = kj - ki + 1
                if newlen <= shortest_running_len:
                    shortest_running_len = newlen
                    shortest_window = (i,j)


            while is_subset and i < j:
                ki = key_indexes[i]
                ic = s[ki]
                
                running_dict[ic] -= 1 # must be in dict and must be > 0... otherwise fatal error. 
                
                i += 1 
                ki = key_indexes[i]
                is_subset = self.is_subset_dict(running_dict, word_dict)
                if is_subset:
                    newlen = kj - ki + 1
                    if newlen <= shortest_running_len:
                        shortest_running_len = newlen
                        shortest_window = (i,j)
                        if newlen == tlen:
                            return s[key_indexes[shortest_window[0]]:key_indexes[shortest_window[1]]+1]

                else:
                    running_dict[ic] += 1  # add key char back in if no longer valid subset.
                    i -= 1

                #print(running_dict)

        if len(shortest_window) == 0:
            return ''

        return s[key_indexes[shortest_window[0]]:key_indexes[shortest_window[1]]+1]


s = Solution()
out = s.minWindow(s='caae', t='cae')
print(out)
     

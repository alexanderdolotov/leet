
from typing import List
#242. Valid Anagram
# 49. Group Anagrams


class Solution:

    def create_char_count(self, s) -> dict:

        cchars = {}
        for c in s:
            if c in cchars:
                cchars[c] += 1
            else:
                cchars[c] = 1 

        return cchars


    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sdict = self.create_char_count(s)
        tdict = self.create_char_count(t)

        for k in sdict.keys():
            snum = sdict.get(k, 0)
            tnum = tdict.get(k, 0)

            if snum != tnum:
                return False 

        return True


    def split_into_same_len(self, strs: List[str]) -> dict:

        grouped_len = {}

        for word in strs:
            wlen = len(word)
            if wlen in grouped_len:
                grouped_len[wlen].append(word)
            else:
                grouped_len[wlen] = [word]

        return grouped_len


    def n2_groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = []

        grouped_indexes = set[int]()

        for i in range(0, len(strs)):

            if i in grouped_indexes:
                continue

            grouping = [strs[i]]
            for j in range(i+1,len(strs)):
                if j in grouped_indexes:
                    continue 

                if self.isAnagram(strs[i], strs[j]):
                    grouping.append(strs[j])
                    grouped_indexes.add(j)
                    grouped_indexes.add(i)

            anagram_groups.append(grouping)

        return anagram_groups

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        same_len = self.split_into_same_len(strs)

        #print(same_len)
        anagram_groups = [] 
        for words in same_len.values():
            anagrams = self.n2_groupAnagrams(words)
            anagram_groups += anagrams

        return anagram_groups



s = Solution()
out = s.groupAnagrams( ["eat","tea","tan","ate","nat","bat", "poopoo", "oopoop"])
print(out)
     



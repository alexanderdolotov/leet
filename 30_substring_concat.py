from typing import List



''' 

30. Substring with Concatenation of All Words
Hard
Topics
premium lock iconCompanies

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

    1 <= s.length <= 10^4
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    s and words[i] consist of lowercase English letters.


'''


class Solution:
        

    def my_word_hash(self, s: str) -> int:
        h = 0
        pow26 = 1
        for c in s:
            h += (ord(c) - ord("a") + 1) * pow26
            pow26 *= 26
        return h


    def my_str_hash(self, s:str, wchunk:int):

        slen = len(s) 
        if slen % wchunk > 0:
            raise Exception('error! error!')

        total_hash = 0 

        for i in range(0, slen, wchunk):
            whash = self.my_word_hash(s[i : i + wchunk])
            total_hash += whash * whash

        return total_hash


        
    def str_hash(self, s: str) -> int:
        
        return self.myhash(s)


    def check_string_in_dict(self, s: str, d: dict, word_len: int) -> bool:

    
        for i in range(0, len(s), word_len):

            word = s[i:i+word_len]

            if word in d and d[word] > 0:

                d[word] -= 1 
            else:
                return False



        return True


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        

        num_words = len(words)
        if num_words < 1:
            return []

        word_len = len(words[0])
        if word_len < 1:
            return []

        slen = len(s)
        if slen < word_len * num_words:
            return []



        word_dict = {}
        word_sum = 0
        for word in words:
            
            if word in word_dict:
                word_dict[word] += 1 
            else:
                word_dict[word] = 1

            for c in word:
                word_sum += ord(c)


        #print('word sum: ', word_sum, 'word_set: ', word_dict)

        # get rolling word sum 
        wolling_word_sum = 0
        for i in range(0,  word_len * num_words):
            wolling_word_sum += ord(s[i])

        #print('starting sum: ', wolling_word_sum)


        results = []


        range_end = slen - word_len * num_words
        for i in range(0, range_end + 1):
            

            # check if sums equal
            if wolling_word_sum == word_sum:
                check_str = s[i:word_len * num_words+i]

                #print('checking for words at ', i, ' ... ', check_str) 

                match_found = self.check_string_in_dict(s=check_str, d=word_dict.copy(), word_len=word_len)
                if match_found: 
                    results.append(i)

            if i == range_end:
                break

            # continue roll:
            wolling_word_sum -= ord(s[i])

            wolling_word_sum += ord(s[i+word_len * num_words])
            

        return results 




s = Solution()
out = s.findSubstring(s='abcdddddabcdefghhhabc', words=['abc'])
print(out)
     

print(s.check_string_in_dict(s='abcabcabc', d={'abc': 2, 'def': 1}, word_len=3))


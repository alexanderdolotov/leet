# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = len(s)
        if l == 0:
            return ''

        
        words = []
        word = ''
        for c in s:
            if c == ' ':
                if len(word) > 0:
                    words.append(word)
                    word = ''
            else:
                word += c 

        if len(word) > 0:
            words.append(word)

        #print(words)

        rstr = ''
        for i in range(len(words)-1, -1, -1):
            if i == 0:
                rstr += words[i]
            else:
                rstr += words[i] + ' '

        
        return rstr



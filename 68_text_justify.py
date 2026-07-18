from typing import List
import math 

'''
68. Text Justification
Hard
Topics
premium lock iconCompanies

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

 

Constraints:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth

 


'''


# beats 100%
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        just = [
            ''
        ]

        i = 0
        for word in words:
            sent = just[i]

            if len(sent) == 0:
                sent += word 
                just[i] = sent
            else:
                if len(word) + len(sent) + 1 > maxWidth:
                    # start new sentence
                    i += 1 
                    just.append(word)
                else: 
                    sent += ' ' + word
                    just[i] = sent


        # final formatting

        print(just)

        just2 = []
        for i in range(0, len(just)):
            sent = just[i]
            diff = maxWidth - len(sent)
            if diff > 0:
                spaces = sent.count(' ')
                if spaces == 0 or i == len(just)-1:
                    just2.append(sent + ' '*diff)
                    continue

                space_incr = int(diff / spaces) 
                
                if diff > 0:
                    remainder = diff - space_incr * spaces
                else:
                    remainder = 0

                #print(spaces, diff, remainder)

                new_sent = ''
                
                for c in sent:
                    if c == ' ':
                        
                        new_sent += ' '*(space_incr + 1)
                        
                        if remainder > 0:
                            new_sent += ' '
                            remainder -= 1 

                        #print(new_sent, space_incr, remainder)

                    else:
                        new_sent += c 

                #print(new_sent)

                just2.append(new_sent)
            else:
                just2.append(sent)


        # extra check 

        # for sent in just2:
        #     if len(sent) != maxWidth:
        #         print('error!', sent)

        return just2


    
s = Solution()
out = s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print(out)


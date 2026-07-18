'''

290. Word Pattern
Easy
Topics
premium lock iconCompanies

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.



'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')
        pats = []
        for c in pattern:
            pats.append(c)

        print(pats, words)

        if len(pats) != len(words):
            return False

        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}

        for a, b in zip(pats, words):
            if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
                return False
        return True



s = Solution()
out = s.wordPattern( pattern = "abba", s = "dog cat cat dog")
print(out)

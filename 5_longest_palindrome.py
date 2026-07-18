'''
5. Longest Palindromic Substring
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, return the longest in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

 

'''


class Solution:
    def longestPalindromeAlex(self, s: str) -> str:
        
        # first pass, store all chars in dict, and keep track of their indexes.
        # characters that occur only once: len of indexes list = 1, cannot be start/end of a Palindrome sequence thats longer than 1...
        # easy: if all chars are unique, longest Palindrome is any character.
        # start from any character thats repeated > 1, and find its other indexes. check if in between string is a palindrom.
        # also palindromes have to be subsets of longer palindromes, and for this, we can keep memory of existing sub-palindromes...
        # this probably runs in n^2

        '''
        Runtime
        1411ms
        Beats28.38%
        Memory
        63.72MB
        Beats5.01%
        '''

        n = len(s)
        if n <= 1:
            return s

        char_indexes = {}
        for i, char in enumerate(s):
            if char not in char_indexes:
                char_indexes[char] = []
            char_indexes[char].append(i)

        # group same-character index pairs by their distance apart, so we can
        # fill the palindrome memo smallest span first
        pairs_by_gap = {}
        for char, indexes in char_indexes.items():
            if len(indexes) < 2:
                continue
            for a in range(len(indexes)):
                for b in range(a + 1, len(indexes)):
                    i = indexes[a]
                    j = indexes[b]
                    gap = j - i
                    if gap not in pairs_by_gap:
                        pairs_by_gap[gap] = []
                    pairs_by_gap[gap].append((i, j))

        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True

        best_start = 0
        best_length = 1

        for gap in sorted(pairs_by_gap.keys()):
            for i, j in pairs_by_gap[gap]:
                if gap == 1 or is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    length = gap + 1
                    if length > best_length:
                        best_length = length
                        best_start = i

        return s[best_start:best_start + best_length]



    def longestPalindromeManacher(self, s: str) -> str:
        # ------------------------------------------------------------------
        # MANACHER'S ALGORITHM — O(n) time, O(n) space.
        #
        # For comparison, the version above is O(n^2) time AND O(n^2) space
        # (that's why it scored low on memory: the dp table and pairs dict
        # both grow with the square of the input, e.g. a string of 1000
        # identical characters allocates a 1000x1000 table). The classic
        # "expand around every center" approach is O(n^2) time, O(1) space.
        # Manacher's algorithm gets all the way down to O(n) time by never
        # re-checking a character it has already proven is part of a
        # palindrome.
        #
        # THE CORE IDEA
        # --------------
        # Expanding around every center independently is wasteful: if we
        # already expanded around some earlier center C and know its
        # palindrome reaches out to a right boundary R, then for a new
        # center i that falls *inside* that palindrome (i < R), the
        # palindrome structure just to the left of C is mirrored exactly
        # to the right of C. So i's mirror position (on the other side of
        # C) tells us a palindrome radius that i is GUARANTEED to already
        # have -- we don't need to re-verify character by character.
        # The only catch: that guarantee only holds up to R (past R we
        # have no information yet), so we cap it there and then continue
        # expanding by brute force from that point on.
        # This "reuse what we already proved" trick is what turns the
        # overall scan from O(n^2) into O(n).
        #
        # ODD vs EVEN LENGTH PALINDROMES
        # -------------------------------
        # Expanding around a center naturally handles odd-length
        # palindromes (one middle character, e.g. "aba"), but even-length
        # ones (two middle characters, e.g. "abba") need a center that
        # sits *between* two characters. Rather than writing two separate
        # cases, we transform the string by inserting a separator between
        # every character (and on both ends). Every palindrome in the
        # transformed string then has odd length, so one code path
        # handles both cases.
        #
        #   original:      a  b  b  a
        #   transformed:  # a #  b  # b # a #
        #   index:        0 1 2  3  4 5 6 7 8
        #
        # "abba" (original indices 0..3) becomes, in the transformed
        # string, the palindrome "#a#b#b#a#" centered at index 4 (the '#'
        # sitting between the two 'b's), extending 4 characters to each
        # side (radius 4).
        #
        # Useful fact we lean on at the end: for a palindrome centered at
        # transformed-index `center` with radius `radius`, its length in
        # the ORIGINAL string is exactly `radius` (not radius*2+1) -- the
        # separators we inserted exactly cancel that out. Check the
        # example above: radius 4 -> original length 4 ("abba"). (correct)
        # ------------------------------------------------------------------

        '''
        Runtime
        35ms
        Beats98.53%
        Memory
        19.32MB
        Beats35.78%
        '''

        if len(s) <= 1:
            return s

        # '#' is safe as a separator: the problem guarantees s only
        # contains digits and English letters, so it can never collide
        # with a real character.
        separator = "#"
        transformed = separator + separator.join(s) + separator
        t_len = len(transformed)

        # radius[i] = how far the palindrome centered at transformed[i]
        # extends to each side. e.g. radius[i] == 2 means
        # transformed[i-2 : i+3] reads the same forwards and backwards.
        radius = [0] * t_len

        # `center` / `right_edge` describe the palindrome (among all
        # palindromes found so far) that reaches furthest to the right:
        # it is centered at `center` and its right end is `right_edge`.
        center = 0
        right_edge = 0

        best_center = 0
        best_radius = 0

        for i in range(t_len):
            if i < right_edge:
                # i sits inside the current best palindrome, so it has a
                # mirror position on the opposite side of `center`.
                mirror = 2 * center - i
                # i is guaranteed to have at least as much radius as its
                # mirror, capped at how far we can currently see
                # (right_edge - i) -- anything past that is unverified.
                radius[i] = min(right_edge - i, radius[mirror])
            else:
                # i is beyond anything we've explored yet; start from 0
                # and rely entirely on brute-force expansion below.
                radius[i] = 0

            # brute-force expand outward from i, one character pair at a
            # time, past whatever radius we started with above
            while True:
                left = i - radius[i] - 1
                right = i + radius[i] + 1
                if left < 0 or right >= t_len:
                    break
                if transformed[left] != transformed[right]:
                    break
                radius[i] += 1

            # if this palindrome reaches further right than our previous
            # best, it becomes the new reference center/right edge
            if i + radius[i] > right_edge:
                center = i
                right_edge = i + radius[i]

            if radius[i] > best_radius:
                best_radius = radius[i]
                best_center = i

        # Map back from the transformed string to the original string.
        # Every other transformed index is a separator, so transformed
        # index t corresponds to original index (t - 1) // 2. The
        # palindrome's original start is therefore:
        start = (best_center - best_radius) // 2
        return s[start:start + best_radius]


    def longestPalindrome(self, s: str) -> str:

        return self.longestPalindromeManacher(s)


if __name__ == "__main__":
    # A few runnable examples so you can see Manacher's algorithm in
    # action. Run this file directly: `python 5_longest_palindrome.py`
    examples = [
        "babad",   # odd-length palindrome: "bab" or "aba" both valid
        "cbbd",    # even-length palindrome: "bb"
        "abba",    # whole string is an even-length palindrome
        "a",       # single character, trivially a palindrome
        "ac",      # no repeats, answer is any single character
        "aaaaa",   # all one character, longest possible palindrome
        "abacdfgdcaba",  # palindrome tucked in the middle: "aba"
    ]

    solution = Solution()
    for example in examples:
        print(f"{example!r:>18} -> {solution.longestPalindromeManacher(example)!r}")


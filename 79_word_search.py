'''
79. Word Search
Medium
Topics
premium lock iconCompanies

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

 

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.


'''

from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        # check that all letters in the word are also on the board
        board_counts = Counter(ch for row in board for ch in row)
        word_counts = Counter(word)
        if any(word_counts[ch] > board_counts[ch] for ch in word_counts):
            return False

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            board[r][c] = '#' # marks temp visited since it matched word char
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i] # sets it back

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


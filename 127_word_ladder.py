'''
127. Word Ladder
Hard
Topics
premium lock iconCompanies

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

Constraints:

    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.

 


'''

class Solution:

    def n2sol(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build graph of word lists, connection points are when a word is one letter difference... 

        # runtime: wordList^2

        wordlen = len(wordList[0]) # # given constraints, is universal len for all words

        def word_dist(word1, word2):
            # given constraints, simple word letter itter
            diffs = 0
            for i in range(0, wordlen):
                diffs += int(word1[i] != word2[i])

            return diffs
        
        if endWord not in set(wordList):
            return 0
        
        wordList.append(beginWord)  # endWord is already there


        word_graph = {}
        for word in wordList:
            for word2 in wordList:

                if word not in word_graph: word_graph[word] = set() # neigbors 

                d = word_dist(word, word2)
                if d == 1: word_graph[word].add(word2)


        # now run BFS from starting word and look for end word 



    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        # use wildcard wordlist struct

        if endWord not in set(wordList):
            return 0
        wordList.append(beginWord)  # endWord is already there

        wordlen = len(beginWord)

        from collections import defaultdict
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(wordlen):
                buckets[word[:i] + '*' + word[i+1:]].append(word)
        # buckets gives you adjacency directly


        from collections import deque

        word_queque = deque([(beginWord, 1)]) # start word 
        visited = {beginWord}

        while word_queque:

            current_word, hops = word_queque.popleft()

            if current_word == endWord:
                return hops 
            
            # check all neighbors 
            for i in range(wordlen):
                neighs = buckets[current_word[:i] + '*' + current_word[i+1:]]
                for n in neighs:
                    if n not in visited:
                        visited.add(n)
                        word_queque.append((n, hops+1))


        return 0


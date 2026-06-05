

from typing import List

'''
274. H-Index
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

'''

# beats 100%
class Solution:


    def hIndex(self, citations: List[int]) -> int:
        
        l = len(citations)

        citations.sort(reverse=False)

        running_hval = 0
        for i in range(0,l):
            p = citations[i]
            if p < 1:
                continue 

            newhval = min(p, l-i)
            if newhval > running_hval:
                running_hval = newhval


        return running_hval
    



s = Solution()
out = s.hIndex([1,3,1])
print(out)


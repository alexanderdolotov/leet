'''
373. Find K Pairs with Smallest Sums
Medium
Topics
premium lock iconCompanies

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

 

Constraints:

    1 <= nums1.length, nums2.length <= 105
    -109 <= nums1[i], nums2[i] <= 109
    nums1 and nums2 both are sorted in non-decreasing order.
    1 <= k <= 104
    k <= nums1.length * nums2.length



'''

from typing import List
import heapq

class Solution:


    def solb(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        '''
        Runtime
        73ms
        Beats85.73%
        Memory
        39.11MB
        Beats85.03%

        '''

        minheap = []
        n = min(k, len(nums1))
        for i in range(n):
            # just run thru first row of k from nums1.... to setup
            minheap.append((nums1[i] + nums2[0], i, 0))
        
        heapq.heapify(minheap) # runs in O(k)

        result = []
        for _ in range(k):
            if not minheap: break
            s, i, j = heapq.heappop(minheap) # pop the smallest sum thus far
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                # append next nums2 candidate into heap. gets sorted out in LgK
                heapq.heappush(minheap, (nums1[i] + nums2[j+1], i, j+1))

        return result


    def soln2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        minheap = []

        # max combos needed, since nums are sorted asc, are bottom k elems from either list
        # this also runs in O(k^2) 
        # but for leetcode: Memory Limit Exceeded 19 / 32 testcases passed

        n = min(k, len(nums1))
        m = min(k, len(nums2))
        for i in range(n):
            n1 = nums1[i]
            for j in range(m):
                n2 = nums2[j]
                minheap.append((n1+n2, n1, n2))


        heapq.heapify(minheap)

        result = []
        for _ in range(k):
            if not minheap: break
            a = heapq.heappop(minheap)
            result.append([a[1], a[2]])

        return result

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
       
        return self.solb(nums1=nums1, nums2=nums2, k=k)
    


'''

4. Median of Two Sorted Arrays
Hard
Topics
premium lock iconCompanies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

 

'''

from typing import List

class Solution:

    def merge(self, nums1: List[int], nums2: List[int]):

        # merges two sorted asc arrays into one sorted array... 

        nums3 = []
        i1 = 0 
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            v1 = nums1[i1]
            v2 = nums2[i2]

            if v1 <= v2:
                nums3.append(v1)
                i1 += 1 
            else:
                nums3.append(v2)
                i2 += 1

        for i in range(i1, len(nums1)):
            nums3.append(nums1[i])

        for i in range(i2, len(nums2)):
            nums3.append(nums2[i])

        return nums3 
    

    def get_median(self, snums: List[int]):

        nlen = len(snums)
        if nlen == 0: return 0

        if nlen % 2 > 0: return snums[nlen // 2]
        else: return ( snums[nlen // 2] + snums[(nlen // 2) - 1]) / 2.0


    def findMedianSortedArrays_MergeOMN(self, nums1: List[int], nums2: List[int]) -> float:

        '''
        Runtime
        6ms
        Beats15.50%
        Memory
        19.54MB
        Beats41.31%
        '''

        merged = self.merge(nums1=nums1, nums2=nums2)

        return self.get_median(merged)
    

    def findMedianSortedArrays_LgMN(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Runtime
        5ms
        Beats18.20%
        Memory
        19.68MB
        Beats14.52%

        '''
        

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 

        return self.findMedianSortedArrays_LgMN(nums1, nums2)
    

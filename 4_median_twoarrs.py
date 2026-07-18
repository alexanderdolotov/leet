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


    def get_median(self, snums: List[int]):

        nlen = len(snums)
        if nlen == 0: return 0

        if nlen % 2 > 0: return snums[nlen // 2]
        else: return ( snums[nlen // 2] + snums[(nlen // 2) - 1]) / 2.0



    def get_disjoint_median(self, snums_a: List[int], snums_b: List[int]):

        # snums_a , snums_b in order 
        alen = len(snums_a)
        blen = len(snums_b)
        tlen = alen + blen 

        m1 = tlen // 2
        v1 = (snums_b[m1 - alen] if m1 >= alen else snums_a[m1])
        
        if tlen % 2 > 0: return v1 
        
        m2 = (tlen // 2) - 1 
        v2 = (snums_b[m2 - alen] if m2 >= alen else snums_a[m2])

        return (v1+v2)/2.0


    def binsearch(self, snums: List[int], target):

        lo, high = 0, len(snums)

        if high == 0: return 0

        m = 0
        while lo < high:
            m = lo + (high-lo) // 2
            v = snums[m]
            if target == v: return m 
            elif target > v: lo = m + 1 
            else: high = m 

       
        return lo # insertion index. if target were to be inserted here





    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # just kick off the recursive version with a window covering the
        # whole of both arrays - no copies made anywhere below this point.
        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        20.06MB
        Beats14.52%
        
        '''

        return self._median_windowed(nums1, 0, len(nums1), nums2, 0, len(nums2))

    def _bounded_search(self, arr: List[int], lo: int, hi: int, target):
        # exactly your binsearch's logic (early-return on an exact match,
        # otherwise the insertion index), except it only ever looks inside
        # arr[lo:hi] and returns an ABSOLUTE index - never slices arr, so
        # this is O(log(hi-lo)) with zero copying, no matter how big arr is.
        while lo < hi:
            mid = lo + (hi - lo) // 2
            v = arr[mid]
            if v == target:
                return mid, True
            elif v < target:
                lo = mid + 1
            else:
                hi = mid
        return lo, False  # lo == hi here: the insertion index

    def _bounded_median(self, arr: List[int], lo: int, hi: int):
        # exactly your get_median's logic, just reading arr[lo:hi] in place
        # instead of being handed an already-sliced copy of it.
        #   arr window = [10,20,30,40,50] (lo=0,hi=5) -> n=5 (odd) -> arr[0+2] = 30
        n = hi - lo
        if n == 0: return 0
        if n % 2 > 0: return arr[lo + n // 2]
        return (arr[lo + n // 2] + arr[lo + n // 2 - 1]) / 2.0

    def _bounded_disjoint_median(self, a_arr: List[int], a_lo: int, a_hi: int, b_arr: List[int], b_lo: int, b_hi: int):
        # exactly your get_disjoint_median's logic (a_arr's window sits
        # entirely below b_arr's window), reading both windows in place.
        #   a-window=[1,2] (a_lo=0,a_hi=2), b-window=[9,10,11] (b_lo=0,b_hi=3)
        #   -> alen=2, tlen=5, m1=2 -> m1(2)>=alen(2) -> v1=b_arr[0+2-2]=b_arr[0]=9
        #   tlen odd -> return 9
        alen = a_hi - a_lo
        tlen = alen + (b_hi - b_lo)

        m1 = tlen // 2
        v1 = b_arr[b_lo + m1 - alen] if m1 >= alen else a_arr[a_lo + m1]

        if tlen % 2 > 0: return v1

        m2 = m1 - 1
        v2 = b_arr[b_lo + m2 - alen] if m2 >= alen else a_arr[a_lo + m2]

        return (v1 + v2) / 2.0

    def _median_windowed(self, A: List[int], alo: int, ahi: int, B: List[int], blo: int, bhi: int) -> float:
        # ================================================================
        # Same algorithm as before, walked through again with
        # nums1=[1,2,3,4,5], nums2=[2,3,4,5,6,7,8] (so alo=0,ahi=5,blo=0,bhi=7
        # on the very first call) - just tracking (lo,hi) index PAIRS into
        # the ORIGINAL nums1/nums2 instead of building new sub-lists every
        # round. Recursing on a smaller window is then just a function call
        # with different integers, not a copy of anything.
        # ================================================================
        alen, blen = ahi - alo, bhi - blo

        # --- trivial cases: same logic as get_median/get_disjoint_median,
        # but through the _bounded_* versions so even these don't copy a
        # potentially-huge window (e.g. nums1=[] with nums2 a million long
        # would otherwise copy all million just to hand it to get_median).
        if alen == 0: return self._bounded_median(B, blo, bhi)
        if blen == 0: return self._bounded_median(A, alo, ahi)

        if A[ahi - 1] <= B[blo]:  # e.g. A-window=[1,2], B-window=[9,10] -> no overlap
            return self._bounded_disjoint_median(A, alo, ahi, B, blo, bhi)

        if B[bhi - 1] <= A[alo]:  # mirror image
            return self._bounded_disjoint_median(B, blo, bhi, A, alo, ahi)

        # s = (array, lo, hi) for the shorter window, l = same for the longer.
        #   A-window=[1,2,3,4,5] (len 5), B-window=[2,3,4,5,6,7,8] (len 7)
        #   -> s = (A, 0, 5), l = (B, 0, 7)
        if alen <= blen:
            s, s_lo, s_hi = A, alo, ahi
            l, l_lo, l_hi = B, blo, bhi
        else:
            s, s_lo, s_hi = B, blo, bhi
            l, l_lo, l_hi = A, alo, ahi

        slen = s_hi - s_lo

        if slen <= 2:
            return self._finish_small(s, s_lo, s_hi, l, l_lo, l_hi)

        # pidx = absolute index of s's own median. pivot = the value there.
        #   s window is A[0:5]=[1,2,3,4,5] -> pidx = 0 + 5//2 = 2, pivot = A[2] = 3
        pidx = s_lo + slen // 2
        pivot = s[pidx]

        # j = absolute index where `pivot` lands inside l's WINDOW (never
        # searches outside [l_lo, l_hi), never copies l).
        #   l window is B[0:7]=[2,3,4,5,6,7,8], pivot=3 -> B[1] is exactly 3, so j=1
        j, is_match = self._bounded_search(l, l_lo, l_hi, pivot)

        # count_left/count_right: identical idea to before, just measured as
        # distances between absolute indices instead of plain lengths.
        #   s's low share:  pidx - s_lo = 2 - 0 = 2   (s's [1,2])
        #   l's low share:  j - l_lo    = 1 - 0 = 1   (l's [2])
        #   count_left = 2 + 1 = 3
        #   s's high share: s_hi-pidx-1 = 5-2-1 = 2   (s's [4,5])
        #   l's high share: l_hi-j-1    = 7-1-1 = 5   (l's [4,5,6,7,8], pivot match skipped)
        #   count_right = 2 + 5 = 7
        count_left = (pidx - s_lo) + (j - l_lo)
        count_right = (s_hi - pidx - 1) + (l_hi - j - (1 if is_match else 0))

        chop = min(count_left, count_right)  # size of whichever pool is smaller

        if count_left <= count_right:
            # low pool is smaller - drop it whole by moving the low ends
            # of both windows up past it (no slicing - just new integers).
            #   new_s_lo = pidx = 2   (drops s's [1,2])
            #   new_l_lo = j    = 1   (drops l's [2])
            new_s_lo, new_l_lo = pidx, j

            # high pool is bigger - only the `chop`=3 most extreme (largest)
            # values get dropped. s_high=[4,5] and l_high=[4,5,6,7,8] are each
            # individually sorted but interleave in VALUE. Walking one element
            # at a time here costs O(chop), which can be O(N) when the two
            # medians land close together (chop close to N/2) - so instead,
            # binary-search for the split: how many of the top `chop` come
            # from l_high (call it `b`) vs s_high (`a=chop-b`). A split is
            # correct once nothing KEPT is bigger than anything TAKEN - same
            # partition idea as the median problem itself, one level deeper.
            s_hi_start = pidx + 1
            l_hi_start = j + (1 if is_match else 0)
            S = s_hi - s_hi_start   # size of s_high = 2  ([4,5])
            L = l_hi - l_hi_start   # size of l_high = 5  ([4,5,6,7,8])

            lo_a, hi_a = max(0, chop - L), min(chop, S)
            while lo_a < hi_a:
                a = lo_a + (hi_a - lo_a) // 2
                b = chop - a
                s_keep_top = s[s_hi - a - 1] if a < S else None      # biggest s would still KEEP
                l_take_bottom = l[l_hi - b] if b > 0 else None       # smallest l would TAKE
                if s_keep_top is not None and l_take_bottom is not None and s_keep_top > l_take_bottom:
                    lo_a = a + 1   # s keeping something bigger than l is taking - take more from s
                else:
                    hi_a = a
            # converges to drop_s_high=0, drop_l_high=3 -> drops l's [6,7,8], same as before
            drop_s_high, drop_l_high = lo_a, chop - lo_a
            new_s_hi, new_l_hi = s_hi - drop_s_high, l_hi - drop_l_high
        else:
            # Mirror image, for when count_right is the smaller pool.
            # Example (different arrays): s-window=[10,20,30], l-window=[1,2,3,4,5,6,7,25,26]
            #   pivot=20, j lands right after the 7 -> count_left=8, count_right=3
            #   count_right is smaller -> drop the WHOLE high pool right away:
            #   s's [30] and l's [25,26] - just move both high boundaries in.
            new_s_hi, new_l_hi = pidx + 1, j + (1 if is_match else 0)

            # ...and only drop the `chop` most extreme (SMALLEST) values from
            # the bigger low pool - same binary-search idea, mirrored: find
            # how many of the bottom `chop` come from l_low (`b`) vs s_low (`a`).
            S = pidx - s_lo   # size of s_low = 1  ([10])
            L = j - l_lo      # size of l_low = 7  ([1,2,3,4,5,6,7])

            lo_a, hi_a = max(0, chop - L), min(chop, S)
            while lo_a < hi_a:
                a = lo_a + (hi_a - lo_a) // 2
                b = chop - a
                s_keep_bottom = s[s_lo + a] if a < S else None       # smallest s would still KEEP
                l_take_top = l[l_lo + b - 1] if b > 0 else None      # biggest l would TAKE
                if s_keep_bottom is not None and l_take_top is not None and s_keep_bottom < l_take_top:
                    lo_a = a + 1   # s keeping something smaller than l is taking - take more from s
                else:
                    hi_a = a
            # converges to drop_s_low=0, drop_l_low=3 -> drops l's [1,2,3], same as before
            drop_s_low, drop_l_low = lo_a, chop - lo_a
            new_s_lo, new_l_lo = s_lo + drop_s_low, l_lo + drop_l_low

        # Recurse on the shrunk windows - just 4 integers change, nothing is
        # copied. Continuing the running example: next call has an A-window
        # of [3,4,5] (indices 2:5) and a B-window of [3,4,5] (indices 1:4).
        if s is A:
            return self._median_windowed(A, new_s_lo, new_s_hi, B, new_l_lo, new_l_hi)
        return self._median_windowed(A, new_l_lo, new_l_hi, B, new_s_lo, new_s_hi)

    def _finish_small(self, s: List[int], s_lo: int, s_hi: int, l: List[int], l_lo: int, l_hi: int) -> float:
        # ================================================================
        # Shorter window (s) is down to 1 or 2 elements. Rather than
        # merging everything, just work out where s's element(s) land
        # inside l's window and read the answer off directly - the only
        # slicing anywhere in this whole solution happens here, and only
        # on these tiny leftover windows.
        #
        # Fresh small example just for this part: s-window=[25,35] (s_lo=0),
        # l-window=[10,20,30,40,50] (l_lo=0):
        #   idx0 = where 25 lands in l -> between 20 and 30 -> idx0=2 (absolute)
        #   idx1 = where 35 lands in l -> between 30 and 40 -> idx1=3 (absolute)
        #   "conceptual" merged array (never actually built in memory):
        #     l[0:2]=[10,20], 25, l[2:3]=[30], 35, l[3:5]=[40,50]
        #     = [10, 20, 25, 30, 35, 40, 50]   (7 elements total)
        # ================================================================
        slen, llen = s_hi - s_lo, l_hi - l_lo

        if slen == 1:
            idx0_abs, _ = self._bounded_search(l, l_lo, l_hi, s[s_lo])
            idx0 = idx0_abs - l_lo  # rank of s's element within the conceptual merge
            def val_at(r):
                if r < idx0: return l[l_lo + r]   # ranks before s's element -> from l
                if r == idx0: return s[s_lo]      # this rank IS s's element
                return l[l_lo + r - 1]             # ranks after -> from l, shifted back 1
        else:
            idx0_abs, _ = self._bounded_search(l, l_lo, l_hi, s[s_lo])
            idx1_abs, _ = self._bounded_search(l, l_lo, l_hi, s[s_lo + 1])
            idx0, idx1 = idx0_abs - l_lo, idx1_abs - l_lo
            def val_at(r):
                if r < idx0: return l[l_lo + r]           # r=0,1  -> l[0],l[1]  = 10,20
                if r == idx0: return s[s_lo]              # r=2    -> s[0]       = 25
                if r < idx1 + 1: return l[l_lo + r - 1]   # r=3    -> l[2]       = 30
                if r == idx1 + 1: return s[s_lo + 1]      # r=4    -> s[1]       = 35
                return l[l_lo + r - 2]                    # r=5,6  -> l[3],l[4] = 40,50

        # total elements currently in play, and which rank(s) the median sits at.
        #   total=7 (odd) -> mid=3 -> val_at(3) = l[3-1] = l[2] = 30 -> median = 30
        total = slen + llen
        mid = total // 2
        if total % 2 == 1:
            return float(val_at(mid))
        else:
            # even total: average the two middle ranks, e.g. total=8 would
            # average val_at(3) and val_at(4) together.
            return (val_at(mid - 1) + val_at(mid)) / 2.0


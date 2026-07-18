from typing import List

'''
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5


'''



class Solution:


    def trap_r(self, height: List[int], begin_idx, stop_idx) -> int:
    
        #print('running for input: ', str(height), 'from: ', begin_idx, 'to: ', stop_idx)
        l = stop_idx - begin_idx + 1

        #input()

        if l <= 2:
            return 0 
        
        if l == 3:
            hr = height[stop_idx]
            hm = height[begin_idx+1]
            hl = height[begin_idx]

            # check if middle is lower than both edges:
            if hm < hl and hm < hr:
                # find second highest:
                if hr <= hl:
                    second_highest = hr 
                else:
                    second_highest = hl 

                return second_highest - hm

            else:
                return 0

        # divide and conquer . find highest, and second highest peak. then run trap for areas to left and right of valley. 

        highest = 0 
        h1_idx = -1
        second_highest = 0 
        h2_idx = -1 

        min_height = None
        monotonic_run_asc_end_idx = 0
        monotonic_run_asc = True

        monotonic_run_desc_end_idx = 0
        monotonic_run_desc = True

        prevh = None
        for i in range(begin_idx, stop_idx+1):

            h = height[i]
            if prevh is not None:
                if h >= prevh and monotonic_run_asc:
                    monotonic_run_asc_end_idx += 1
                else:
                    monotonic_run_asc = False

                if h <= prevh and monotonic_run_desc:
                    monotonic_run_desc_end_idx += 1
                else:
                    monotonic_run_desc = False

            if h > highest:
                second_highest = highest
                h2_idx = h1_idx 

                highest = h 
                h1_idx = i 

            elif h > second_highest:
                second_highest = h 
                h2_idx = i

            if min_height is None:
                min_height = h 

            if h < min_height:
                min_height = h

            prevh = h

        
        if monotonic_run_asc_end_idx == stop_idx:
            print('monotonic ascending run detected at end of array')
            return 0

        if monotonic_run_desc_end_idx == stop_idx:
            print('monotonic descending run detected at end of array')
            return 0


        #print('stats:', h1_idx, highest, h2_idx, second_highest,  min_height)
        
        if h1_idx < 0 or h2_idx < 0:
            return 0 
        
        
        # if secon highest peak is at floor, no water can be held.
        if second_highest - min_height == 0:
            return 0
        
        start_idx = (h1_idx if h1_idx < h2_idx else h2_idx)
        end_idx = (h1_idx if h1_idx >= h2_idx else h2_idx)
        
        if abs(h1_idx - h2_idx) <= 1:
            larea = self.trap_r(height=height, begin_idx=begin_idx, stop_idx=start_idx)
            rarea = self.trap_r(height=height, begin_idx=end_idx, stop_idx=stop_idx)
            return larea + rarea
        
        # count in between 
        area = 0
        for i in range(start_idx+1, end_idx):
            area += second_highest - height[i]

        #print('found area: ', area)

        larea = self.trap_r(height=height, begin_idx=begin_idx, stop_idx=start_idx)
        rarea = self.trap_r(height=height, begin_idx=end_idx, stop_idx=stop_idx)
        return area + larea + rarea
    

    def trap(self, height: List[int]) -> int:
        return self.trap_r(height, 0, len(height)-1)
        

s = Solution()
out = s.trap([4,2,0,3,2,5])
print(out)


from typing import List


'''
57. Insert Interval
Medium
Topics
premium lock iconCompanies
Hint

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



'''


class Solution:

    def linear_sol2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # runtime beats 100%

        results = []
        merging_interval = None
        ended_merge = False
        for i in range(0, len(intervals)):
            oldi = intervals[i]

            if ended_merge:
                results.append(oldi)
                continue

            if merging_interval is None:
                if newInterval[0] < oldi[0] and newInterval[1] >= oldi[0]:
                    oldi[0] = newInterval[0]

                if newInterval[0] <= oldi[1] and newInterval[0] >= oldi[0]:
                    merging_interval = oldi 

                # if new interval fits perfectly inside an interval
                if newInterval[0] >= oldi[0] and newInterval[1] <= oldi[1]:
                    return intervals

                if newInterval[1] < oldi[0]:
                    results.append(newInterval)
                    ended_merge = True

                results.append(oldi)


            else:
                # there is a prior merging interval, so only look for ending

                if newInterval[1] < oldi[0]: # if ending of new interval is less than start of this one
                    merging_interval[1] = newInterval[1]
                    ended_merge = True
                    results.append(oldi)
                elif newInterval[1] <= oldi[1]:
                    merging_interval[1] = oldi[1]
                    ended_merge = True
                    # do not append interval, so as to merge it


        if not ended_merge:
            results[-1][1] = newInterval[1]


        return results



    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        # check edge cases first 
        ilen = len(intervals)
        nilen = len(newInterval)
        if ilen == 0:
            if nilen > 0:
                return [newInterval] 
            else:
                return []

        if nilen == 0:
            return intervals

        lowest = intervals[0][0]
        highest = intervals[-1][1]

        if newInterval[0] <= lowest and newInterval[1] >= highest:
            return [newInterval]

        if newInterval[0] > highest:
            intervals.append(newInterval)
            return intervals 

        if newInterval[0] >= highest:
            intervals[-1][1] = newInterval[1]
            return intervals 

        if newInterval[1] < lowest:
            return (  [newInterval] + intervals)

        if newInterval[1] <= lowest:
            intervals[0][0] = newInterval[0]
            return intervals


        return self.linear_sol2(intervals=intervals, newInterval=newInterval)




s = Solution()

#intervals = [[1,3],[6,9]]
#newInterval = [2,5]

intervals = [[3,5],[12,15]]
newInterval = [6,16]

out = s.insert(intervals, newInterval)

print(out)



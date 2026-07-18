'''
295. Find Median from Data Stream
Hard
Topics
premium lock iconCompanies

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

 

Constraints:

    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

 

Follow up:

    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?



'''

from typing import List
import heapq


class MedianFinder:

    def __init__(self):
        self.maxheap = []  # lower half, values negated
        self.minheap = []  # upper half
        self.mediannum = None

        '''
        Runtime
        146ms
        Beats87.57%
        Memory
        42.30MB
        Beats35.17%
        '''

    def addNum(self, num: int) -> None:

        if self.mediannum is None: # no median currently
            if self.maxheap and num < -self.maxheap[0]:
                heapq.heappush(self.maxheap, -num)
                self.mediannum = -heapq.heappop(self.maxheap)
            elif self.minheap and num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
                self.mediannum = heapq.heappop(self.minheap)
            else:
                self.mediannum = num # if heaps are empty, 1st value is median.
        else:
            if num <= self.mediannum:
                heapq.heappush(self.maxheap, -num) # push smaller number unto maxheap
                heapq.heappush(self.minheap, self.mediannum) # push the old median unto minheap
            else:
                heapq.heappush(self.minheap, num)
                heapq.heappush(self.maxheap, -self.mediannum)
            
            self.mediannum = None # set median to be empty when even elements

    def findMedian(self) -> float:
        if self.mediannum is not None:
            return float(self.mediannum)
        return (-self.maxheap[0] + self.minheap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


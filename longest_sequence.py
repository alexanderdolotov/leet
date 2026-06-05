from dataclasses import dataclass
from typing import List

'''
128. Longest Consecutive Sequence
Medium
Topics
premium lock iconCompanies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3




'''



@dataclass
class Seq:
    """Inclusive consecutive integer range [start, end].

    ``Seq(n)`` is a single-element range; ``Seq(start, end)`` is the full span.
    """

    start: int
    end: int | None = None

    def __post_init__(self) -> None:
        if self.end is None:
            self.end = self.start

    def __str__(self) -> str:
        assert self.end is not None
        return f"Seq(start={self.start}, end={self.end})"

    def __repr__(self) -> str:
        return str(self)

    @property
    def length(self) -> int:
        assert self.end is not None
        return self.end - self.start + 1


    def add_num(self, num:int):
        if num < self.start:
            self.start = num 

        if num > self.end:
            self.end = num

        return True
        
        


class Solution:

    
    def seq_sol(self, nums: List[int]) -> int:

        seq_dict: dict[int, Seq] = {}

        for num in nums:
            
            if num not in seq_dict:
                
                # check if neighbors exist 
                num_p1 = num + 1
                num_m1 = num -1 

                running_start = num 
                running_end = num 

                if num_p1 in seq_dict:
                    num_p1_sq = seq_dict[num_p1]
                    num_p1_sq.add_num(num)
                    running_start = min(running_start, num_p1_sq.start)
                    running_end = max(running_end, num_p1_sq.end)

                if num_m1 in seq_dict:
                    num_m1_sq = seq_dict[num_m1]
                    num_m1_sq.add_num(num_m1)
                    running_start = min(running_start, num_m1_sq.start)
                    running_end = max(running_end, num_m1_sq.end)

                # create new sequence if no others found
                if running_start == running_end == num:
                    seq_dict[num] = Seq(num)
                    
                else:
                    
                    if running_start not in seq_dict:
                        
                        endsq = seq_dict[running_end]
                        endsq.add_num(running_start)
                        seq_dict[running_start] = endsq
                    else:
                        
                        seq_dict[running_start].add_num(running_end)
                    
                    if running_end not in seq_dict:
                        
                        startsq = seq_dict[running_start]
                        startsq.add_num(running_end)
                        seq_dict[running_end] = startsq
                    else:
                        
                        seq_dict[running_end].add_num(running_start)
            

        max_len = 1 
        for s in seq_dict.values():
            if s.length > max_len:
                max_len = s.length


        return max_len

    def longestConsecutive(self, nums: List[int]) -> int:
        
        nlen = len(nums)

        if nlen == 0:
            return 0 

        if nlen == 1:
            return 1

        return self.seq_sol(nums)



s = Solution()
out = s.longestConsecutive([0,1,2,4,5,7])
print(out)
     



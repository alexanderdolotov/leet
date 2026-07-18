'''
23. Merge k Sorted Lists
Hard
Topics
premium lock iconCompanies

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.



'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


    def _merge2_lists(self, listnode1: Optional[ListNode], listnode2: Optional[ListNode]):
        dummy = ListNode(-1)
        cur = dummy
        while listnode1 and listnode2:
            if listnode1.val <= listnode2.val:
                cur.next = listnode1
                listnode1 = listnode1.next
            else:
                cur.next = listnode2
                listnode2 = listnode2.next
            cur = cur.next
        cur.next = listnode1 or listnode2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        '''
        Runtime
        11ms
        Beats55.07%
        Memory
        22.55MB
        Beats92.97%

        
        '''

        # 2 ways to go about this... 1 is to handle 2 lists at a time, and keep doing merge sort
        # second way is to try to do all k lists at the same time... finding min value and incrementing pointers, and balancing lengths...
        # 1st way seems way easier... and lists can be subsplit... so merge pairs first
        L = len(lists)

        if L == 1:
            return lists[0]

        new_lists = []
        for i in range(0, L, 2):
            l2 = lists[i+1] if i+1 < L else None  # odd-length: last list has no pair
            nl = self._merge2_lists(listnode1=lists[i], listnode2=l2)
            new_lists.append(nl)

        if len(new_lists) > 1:
            return self.mergeKLists(new_lists)
        else:
            return new_lists[0]
    




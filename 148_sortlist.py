'''

148. Sort List
Medium
Topics
premium lock iconCompanies

Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105

 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
 

'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def sortList_A1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Runtime
        180ms
        Beats44.86%
        Memory
        40.68MB
        Beats60.48%

        
        '''

        # recursive merge sort: split at midpoint via slow/fast pointers, sort halves, merge
        if not head or not head.next:
            return head

        # use slow/fast method to find mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next 
        slow.next = None # break up the list into 2 lists

        # recursively sort the halves... 
        left = self.sortList_A1(head)
        right = self.sortList_A1(mid)
        return self._merge(left, right)

   
    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # create a dummy start just as a convenient placeholder
        tail = dummy # tail = current node

        # merges 2 sorted linked lists by iteratig over both at the same time and comparing next value
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2 # append the remaining list if exists
        return dummy.next # returns the start of sorted list



    def sortList_A2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Runtime
        212ms
        Beats17.02%
        Memory
        40.82MB
        Beats19.58%
        
        '''
        # bottom-up iterative merge sort: O(n log n) time, O(1) extra space
        if not head or not head.next:
            return head

        # finds length of entire list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # basically start by sorting pairs in the list first, 
        # [9,8,7,6,5,4,3,2,1] -> [8,9 , 6,7 , 4,5 , 2,3 , 1]
        # then mergesort in 4s -> [6,7,8,9 , 2,3,4,5 , 1]
        # keep moving up, merge sort 8s -> [2,3,4,5,6,7,8,9, 1]
        # complete remainders: [1,2,3,4,5,6,7,8,9]

        dummy = ListNode(0, head)
        size = 1
        while size < length:
            prev, curr = dummy, dummy.next
            while curr:
                left = curr
                right = self._split(left, size)
                curr = self._split(right, size)
                prev = self._merge_from(left, right, prev)
            size *= 2

        return dummy.next
    
    def _split(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cuts off the first n nodes starting at head, returns the head of the remainder
        for _ in range(n - 1):
            if not head:
                break
            head = head.next
        if not head:
            return None
        rest = head.next
        head.next = None
        return rest

    def _merge_from(self, l1: Optional[ListNode], l2: Optional[ListNode], prev: ListNode) -> ListNode:
        # merges l1/l2, attaches result after prev, returns the new tail
        tail = prev
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        while tail.next:
            tail = tail.next
        return tail



    def sortList_A3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # extract values, sort with Python's built-in (C-level Timsort), write back in place
        # trades the O(1) space follow-up constraint for O(n) space in exchange for speed

        '''
        Runtime
        20ms
        Beats94.88%
        Memory
        40.74MB
        Beats34.97%
        
        '''

        node = head
        values = []
        while node:
            values.append(node.val)
            node = node.next

        values.sort() # uses C to sort data fast

        node = head
        i = 0
        while node:
            node.val = values[i]
            node = node.next
            i += 1

        return head
    

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortList_A1(head)


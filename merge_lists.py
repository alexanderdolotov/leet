

'''
21. Merge Two Sorted Lists
Easy
Topics
premium lock iconCompanies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

 

'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        
        running_l1 = list1 
        running_l2 = list2 
        start = None
        sorted = None 

        while True:

            if running_l1 is None and running_l2 is None:
                return start
            

            if running_l1 is not None and running_l2 is not None:
                if running_l1.val < running_l2.val:
                    if sorted:
                        sorted.next = running_l1
                        sorted = sorted.next
                    else:
                        sorted = running_l1 
                        start = sorted

                    running_l1 = running_l1.next 

                else:
                    if sorted:
                        sorted.next = running_l2
                        sorted = sorted.next
                    else:
                        sorted = running_l2
                        start = sorted

                    running_l2 = running_l2.next

            elif running_l1 is not None:
                if sorted:
                    sorted.next = running_l1
                    sorted = sorted.next
                else:
                    sorted = running_l1 
                    start = sorted

                running_l1 = running_l1.next 

            elif running_l2 is not None:
                if sorted:
                    sorted.next = running_l2
                    sorted = sorted.next
                else:
                    sorted = running_l2 
                    start = sorted

                running_l2 = running_l2.next 




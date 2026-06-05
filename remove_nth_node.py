
'''
19. Remove Nth Node From End of List
Medium
Topics
premium lock iconCompanies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

 

Follow up: Could you do this in one pass?
 

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def onsol(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # somehow this beats 100% ... even tho is 2N runtime

        # find length
        dummy = ListNode(-1, head)
        i = 0
        cur = dummy 
        while cur:
            i += 1 
            cur = cur.next 

        print('total len: ', i)


        # go to n-1 node:
        cur = dummy 
        for k in range(i-n-1):
            cur = cur.next 

        print('at k: ', cur.val)
        if cur.next:
            cur.next = cur.next.next 

        return dummy.next


    def one_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # keep a second pointer of n+1 nodes behind.... 

        # in practice, since 2 pointerss are always being updated, still runs in 2N


        return None



    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        return self.onsol(head, n) 





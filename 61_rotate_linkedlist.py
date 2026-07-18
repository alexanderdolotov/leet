
'''
61. Rotate List
Medium
Topics
premium lock iconCompanies

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10*9

 


'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_length(self, head) :
       
        # returns length and last node
        i = 1
        cur = head 
        while cur.next:
            cur = cur.next 
            i += 1

        return i, cur


    def break_right(self, head: Optional[ListNode], b) -> Optional[ListNode]:
       
        # breaks the chain in the list at b
        cur = head
        for i in range(0, b-1):

            cur = cur.next 

        start = cur.next
        cur.next = None

        return start



    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head: return head 
        if not head.next: return head 


        listn, lastnode = self.get_length(head)

        rotations = k % listn 
        if rotations == 0:
            return head

        # loop back last node
        lastnode.next = head

        print('rotations: ', rotations)

        return self.break_right(head, b=listn-rotations)


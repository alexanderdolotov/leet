'''
82. Remove Duplicates from Sorted List II
Medium
Topics
premium lock iconCompanies

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.




'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def usehashsol(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # beats 100% 
        valcounts = {}

        cur = head 
        i = 0
        while cur:

            if cur.val in valcounts:
                valcounts[cur.val] += 1 
            else:
                valcounts[cur.val] = 1 

            cur = cur.next 
            i += 1


        # second pass... remove dups 

        dummy = ListNode(-1,None)

        cur = head 
        ucur = dummy
        for k in range(i):

            if valcounts[cur.val] == 1:
                ucur.next = cur 
                ucur = cur 
            
            cur = cur.next

        ucur.next = None

        return dummy.next



    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return head 
        if head.next is None: return head 


        return self.usehashsol(head)






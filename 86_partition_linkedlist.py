
'''
86. Partition List
Medium
Topics
premium lock iconCompanies

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

 

Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def onmemsol(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        
        # create 2 stacks of less than and >= x 
        ltnodes = []
        gtnodes = []

        cur = head 
        i = 0
        while cur:

            v = cur.val 
            i += 1 

            if v < x:
                ltnodes.append(cur)
            else:
                gtnodes.append(cur)

            cur = cur.next

        # create new chain 

        total_list = ltnodes + gtnodes

        prev = None
        for t in total_list:

            t.next = None
            if prev:
                prev.next = t

            prev = t



        return total_list[0]


    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head: return head 
        if not head.next: return head 

        return self.onmemsol(head, x) 





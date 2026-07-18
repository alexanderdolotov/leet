

'''
25. Reverse Nodes in k-Group
Hard
Topics
premium lock iconCompanies

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

 

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

 

Follow-up: Can you solve the problem in O(1) extra memory space?
 

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:



    def neatcode_reverse(self, head: ListNode, left: int, right: int) :

        dummy = ListNode(0, head)

        leftPrev = dummy
        cur = head 
        for i in range(left-1):
            leftPrev = cur 
            cur = cur.next 

            if cur is None: # if list is too short, do not reverse
                return dummy.next, None

        # check that range exists
        cur1 = cur
        for i in range(right-left+1):

            if cur1 is None: # if list is too short, do not reverse
                return dummy.next, None

            cur1 = cur1.next


        cur1 = None

        lnext = leftPrev.next
        prev = None 
        for i in range(right-left+1):
            
            tmpNext = cur.next 
            cur.next = prev 
            prev = cur
            cur = tmpNext


        lnext.next = cur

        leftPrev.next = prev

        return dummy.next, lnext



    def neatcode_loopr(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reusing the previous question reverse_linked_list.py answer to loop over iteratively...

        start, end = self.neatcode_reverse(head, 1, k)

        if start and end:
            print(start.val, end.val )
        else:
            return head

        
        current = end
        while current and end:
            
            start2, end2 = self.neatcode_reverse(current.next, 1, k)
             
            if start2 and end2:
                print(start2.val, end2.val )
                current.next = start2
                current = end2
            else:
                break

            

        return start
            


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        if head is None:
            return head

        if k == 1:
            return head


        return self.neatcode_loopr(head, k)




sol = Solution()
out = sol.reverseKGroup(ListNode(1), k=5)




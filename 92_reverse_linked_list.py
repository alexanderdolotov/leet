

'''
92. Reverse Linked List II
Medium
Topics
premium lock iconCompanies

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

 

Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:


    # times out on memory limits
    def reverse_listmem(self, head: ListNode, left: int, right: int) -> ListNode:

        # works but runs out of memory
        print('running reverse_listmem')
        nodes_to_reverse : list[ListNode] = [] # mem intensive 
        current_node = head
        start_node = head

        for i in range(1, right+1):

            if i >= left:
                nodes_to_reverse.append(current_node)
            elif i < left:
                start_node = current_node

            current_node = current_node.next

        #print(start_node, len(nodes_to_reverse))
        # set first node to point to last node:

        if len(nodes_to_reverse) == 0:
            return head 

        nodes_to_reverse[0].next = nodes_to_reverse[-1].next
        start_node.next = nodes_to_reverse[-1]

        for i in range(len(nodes_to_reverse)-1, 0, -1):
            nodes_to_reverse[i].next = nodes_to_reverse[i-1]


        return head 


    def neatcode_reverse(self, head: ListNode, left: int, right: int) -> ListNode:

        dummy = ListNode(0, head)

        leftPrev = dummy
        cur = head 
        for i in range(left-1):
            leftPrev = cur 
            cur = cur.next 


        lnext = leftPrev.next
        prev = None 
        for i in range(right-left+1):
            tmpNext = cur.next 
            cur.next = prev 
            prev = cur
            cur = tmpNext

        lnext.next = cur

        leftPrev.next = prev


        return dummy.next


    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if head is None:
            return head 

        if right - left == 0:
            return head 



        return self.neatcode_reverse(head, left, right)




sol = Solution()
out = sol.reverseBetween(ListNode(1), 3,5)


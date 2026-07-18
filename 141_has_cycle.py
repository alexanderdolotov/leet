
'''
141. Linked List Cycle
Easy
Topics
premium lock iconCompanies

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

 

Follow up: Can you solve it using O(1) (i.e. constant) memory?


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def nmem_hascycle(self, head) -> bool:
        
        if head is None:
            return False 
        
        if head.next is None:
            return False

        seen_nodes = set()
        running_node = head
        seen_nodes.add(running_node)
        for i in range(10001):

            if running_node.next is None:
                return False

            running_node = running_node.next 
            if running_node in seen_nodes:
                return True
            
            seen_nodes.add(running_node)

        return False
    
    def const_mem_has_cycle(self, head) -> bool:

        if head is None:
            return False 
        
        if head.next is None:
            return False
        
     
        running_node = head
        for i in range(10001): # the max constraint is 10^4... so just loop that much, if more, there us cycle. 

            if running_node.next is None:
                return False

            running_node = running_node.next 
            
        return True
    

    

    def has_cycle_constmem_nruntime(self, head) -> bool:

        # beats 92% runtime, 99% mem. destroys linked list in the process

        honeytrap = ListNode()

        running_node = head 
        prev_node = None
        for _ in range(10001):

            if not running_node:
                return False

            if not running_node.next:
                return False
            
            if running_node.next is honeytrap:
                return True
            
            prev_node = running_node
            running_node = running_node.next # break up the chain by setting honey trap in previous visitied nodes. 

            prev_node.next = honeytrap


        return True
    

    def slowfast(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        # Using 'is' for speed and 'fast.next' check for the leap
        while fast is not slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True


    def hasCycle(self, head) -> bool:
        
    
        return self.slowfast(head)
    

sol = Solution()
out = sol.hasCycle([3,2,0,-4])
print(out)

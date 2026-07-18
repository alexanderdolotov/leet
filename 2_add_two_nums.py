

'''
2. Add Two Numbers
Medium
Topics
premium lock iconCompanies

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

 


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        running_l1 = l1 
        running_l2 = l2 
        running_val = 0
        carryover = 0

        current_node = None
        starting_node = None

        while True:

            if running_l1 is None and running_l2 is None:
                if carryover > 0 and current_node is not None:
                    current_node.next =  ListNode(val=carryover)

                return starting_node
            

            if current_node is not None:
                current_node.next = ListNode(val=0)
                current_node = current_node.next
            else:
                current_node = ListNode(val=0)
                starting_node = current_node
            

            val1 = 0
            val2 = 0
            if running_l1 is not None:
                val1 = running_l1.val 
                running_l1 = running_l1.next 

            if running_l2 is not None:
                val2 = running_l2.val 
                running_l2 = running_l2.next 

            
            running_val = val1 + val2 + carryover
            carryover = 0
            
            if running_val >= 10:
                carryover = running_val // 10
                running_val = running_val - 10

            #print('running_val', running_val, carryover)
            current_node.val = running_val
            
    


sol = Solution()
l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=8)))

out = sol.addTwoNumbers(l1 = l1, l2 = l2)

print(out.val)
print(out.next.val)
print(out.next.next.val)
print(out.next.next.next.val)

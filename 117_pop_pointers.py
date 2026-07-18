
'''
117. Populating Next Right Pointers in Each Node II
Medium
Topics
premium lock iconCompanies

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100

 

'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:


    level_map = [[]]
    
    def _build_lmap(self, node, level):

        if level >= len(self.level_map): # increase levels if new level is found.
            self.level_map.append([])

        level_nodes = self.level_map[level]

        level_nodes.append(node)

        if node.left:
            self._build_lmap(node.left, level+1)

        if node.right:
            self._build_lmap(node.right, level+1)
        



    def connect_lmap(self, root: Node) -> Node:

        if root:
            self._build_lmap(root, 0)

        #print(self.level_map)

        # connect same level nodes:
        for l in range(0, len(self.level_map)):
            lnodes = self.level_map[l]
            if len(lnodes) > 1:
                for i in range(0, len(lnodes)-1):
                    lnodes[i].next = lnodes[i+1]
        
        return root



    def connect_optimal(self, root: Node) -> Node:
        curr = root
        while curr:
            dummy = Node(0)
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root
    
    def connect(self, root: Node) -> Node:
        return self.connect_optimal(root)


sol = Solution()
x = sol.connect(root=Node())

print(x)



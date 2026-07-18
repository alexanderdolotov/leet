'''

427. Construct Quad Tree
Medium
Topics
premium lock iconCompanies

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
    isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

    If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
    If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
    Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

    n == grid.length == grid[i].length
    n == 2x where 0 <= x <= 6


'''



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from typing import List, Optional

class Solution:

    def construct_A1(self, grid: List[List[int]]) -> 'Node':

        '''
        Runtime
        115ms
        Beats5.20%
        Memory
        20.00MB
        Beats71.82%

        
        '''

        # since the grid is of size 2^n X 2^n, we can just split into 4 quadrants and recurse downwards.

        L = len(grid)
        if L == 1:
            return Node(
                val=grid[0][0],
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None
                )

        # split into 4 quadrant copies (simpler than tracking index bounds, costs extra memory)
        half = L // 2
        top_left = [row[:half] for row in grid[:half]]
        top_right = [row[half:] for row in grid[:half]]
        bottom_left = [row[:half] for row in grid[half:]]
        bottom_right = [row[half:] for row in grid[half:]]

        tl = self.construct(top_left)
        tr = self.construct(top_right)
        bl = self.construct(bottom_left)
        br = self.construct(bottom_right)

        # collapse into a single leaf if all 4 children are leaves with the same value
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return Node(
                val=tl.val,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None
                )

        return Node(
            val=True,
            isLeaf=False,
            topLeft=tl,
            topRight=tr,
            bottomLeft=bl,
            bottomRight=br
            )

    def construct_A2(self, grid: List[List[int]]) -> 'Node':
        '''
        Runtime
            95ms
            Beats48.60%
            Memory
            19.89MB
            Beats91.95%

        
        '''

        return self._build(grid, 0, len(grid), 0, len(grid))

    def _build(self, grid: List[List[int]], r0: int, r1: int, c0: int, c1: int) -> 'Node':

        # sanity check on first pass: scan region — if uniform, return leaf immediately without splitting
        first = grid[r0][c0]
        uniform = True
        for r in range(r0, r1):
            for c in range(c0, c1):
                if grid[r][c] != first:
                    uniform = False
                    break
            if not uniform:
                break

        if uniform:
            return Node(val=bool(first), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)

        # not uniform — split into 4 quadrants by midpoint and recurse (no copies, just index bounds)
        mid_r = (r0 + r1) // 2
        mid_c = (c0 + c1) // 2

        tl = self._build(grid, r0,   mid_r, c0,   mid_c)
        tr = self._build(grid, r0,   mid_r, mid_c, c1)
        bl = self._build(grid, mid_r, r1,   c0,   mid_c)
        br = self._build(grid, mid_r, r1,   mid_c, c1)

        # no collapse check needed: if all 4 quadrants were uniform with the same value,
        # the parent region would have been caught as uniform above and never split
        return Node(val=True, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl, bottomRight=br)


    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.construct_A2(grid)
    

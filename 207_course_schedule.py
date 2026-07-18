'''
207. Course Schedule
Medium
Topics
premium lock iconCompanies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

 
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list: course -> list of its prerequisites
        graph = {}
        for course, prereq in prerequisites:
            graph.setdefault(course, []).append(prereq)

        # 3-color DFS state per node: 1 = in-progress (on stack), 2 = safe (fully explored)
        state = {}

        def dfs(node):
            if node in state:
                # memoization: already resolved — safe if state is 2, cycle if state is 1
                return state[node] == 2
            state[node] = 1  # mark in-progress
            for neighbor in graph.get(node, []):
                if not dfs(neighbor):
                    return False  # cycle detected, propagate up immediately
            state[node] = 2  # all neighbors safe, mark this node safe
            return True

        # all() short-circuits: returns False the moment any dfs() returns False,
        # equivalent to a for loop with an early return
        return all(dfs(node) for node in graph)

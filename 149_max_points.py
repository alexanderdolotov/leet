'''
149. Max Points on a Line
Hard
Topics
premium lock iconCompanies

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 

Constraints:

    1 <= points.length <= 300
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All the points are unique.

 


'''

from typing import List


def is_collinear(p1, p2, p3):
    '''
    The idea: compare slopes without dividing.

    Three points p1, p2, p3 are collinear exactly when the slope from p1→p2 equals the slope from p1→p3. 
    Slope is normally rise/run (dy/dx), but division is risky here — a vertical line has dx = 0, which would crash. 
    So instead of comparing dy1/dx1 == dy2/dx2, 
        the code cross-multiplies to avoid dividing at all: dx1 * dy2 == dx2 * dy1.
    
    '''

    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])


class Solution:

    def sol_n2(self, points: List[List[int]]) -> int:

        '''
        Runtime
        240ms
        Beats9.63%
        Memory
        31.82MB
        Beats7.99%
        
        '''


        n = len(points)
        if n <= 2:
            return n

        def slope_key(a, b):
            dx = points[b][0] - points[a][0]
            dy = points[b][1] - points[a][1]
            if dx == 0:
                return float('inf')
            return dy / dx

        slope_points = {} # slope -> set of point indices sharing that slope with some other point

        # runs in n^2
        for p1 in range(0, n):

            for p2 in range(p1 + 1, n):

                # slope can include infinity (vertical line)
                slope = slope_key(p1, p2)

                slope_points.setdefault(slope, set()).update((p1, p2)) # update not add?

        # sort slopes in desc order by num points sharing that slope
        slope_order = sorted(slope_points.items(), key=lambda kv: len(kv[1]), reverse=True)

        # in desc order, iterate thru slopes with most common points, and find the longest possible line among those points.
        # keep the max running points line. stop iterating once next slope's num points <= length of best running line
        best = 1

        for slope, pt_set in slope_order:

            if len(pt_set) <= best:
                break # no remaining (smaller) bucket can beat the current best

            # points sharing this slope aren't necessarily all on the same line
            # (two unrelated pairs can coincidentally share a slope), so find the
            # longest actual line among them using the same anchor technique
            candidates = list(pt_set)
            local_best = 1

            for anchor in candidates:

                counts = {}

                for other in candidates:
                    if other == anchor:
                        continue
                    s = slope_key(anchor, other)
                    counts[s] = counts.get(s, 0) + 1

                if counts:
                    local_best = max(local_best, max(counts.values()) + 1)

                if local_best == len(candidates):
                    break # bucket is fully collinear -- can't do better within it

            best = max(best, local_best)

            if local_best == len(candidates):
                # bucket saturated: buckets are processed in descending size order, so
                # every remaining bucket's size (and thus its local_best) is <= this one's
                return best

        return best


    def sol_n2_anchor(self, points: List[List[int]]) -> int:

        # standard technique: fix each point as an anchor and count slopes to every
        # other point relative to it. slope relative to a fixed anchor uniquely
        # determines the line through that anchor, so no global bucketing/sort needed.
        # O(n^2) time, O(n) space.

        '''
        Runtime
        31ms
        Beats44.63%
        Memory
        19.44MB
        Beats36.95%
        
        '''

        
        n = len(points)
        if n <= 2:
            return n

        best = 1

        for p1 in range(n):

            slope_counts = {}

            for p2 in range(n):
                if p2 == p1:
                    continue

                dx = points[p2][0] - points[p1][0]
                dy = points[p2][1] - points[p1][1]
                slope = float('inf') if dx == 0 else dy / dx

                slope_counts[slope] = slope_counts.get(slope, 0) + 1

            best = max(best, max(slope_counts.values()) + 1)

        return best


    def nfsol(self, points: List[List[int]]) -> int:

        # Time Limit Exceeded 35 / 42 testcases passed

        # this solution is straight forward. iterate thru every point, and try to form a line with every other point.
        # runs in n! time..

        n = len(points)
        if n <= 2:
            return n

        def count_on_line(p1, p2, remaining):
            if not remaining:
                return 0
            head, *rest = remaining
            extra = 1 if is_collinear(p1, p2, head) else 0
            return extra + count_on_line(p1, p2, rest)

        def permute(remaining, chosen):
            if len(chosen) == 3:
                p1, p2, p3 = chosen
                if not is_collinear(p1, p2, p3):
                    return  # trim: p3 doesn't extend the line, no point exploring this branch further

                count = 3 + count_on_line(p1, p2, remaining)
                self.best = max(self.best, count)
                return

            for i in range(len(remaining)):
                permute(remaining[:i] + remaining[i+1:], chosen + [remaining[i]])

        self.best = 2
        permute(points, [])
        return self.best
    





    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) == 0: return 0 
        if len(points) == 1: return 1 # infinite lines cross a single point
        if len(points) == 2: return 2 # any 2 points on 2d plane for a straight line


        return self.sol_n2_anchor(points)
    

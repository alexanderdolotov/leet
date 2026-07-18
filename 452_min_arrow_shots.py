from typing import List


'''

452. Minimum Number of Arrows to Burst Balloons
Medium
Topics
premium lock iconCompanies

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

 

Constraints:

    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= xstart < xend <= 2^31 - 1

 

'''

class Solution:

    
    def get_intersecting_range(self, p1, p2):

        # Fits inside

        if p1[0] >= p2[0] and p1[1] <= p2[1]:
            # p1 is inside p2
            return p1 

        if p1[0] <= p2[0] and p1[1] >= p2[1]:
            # p2 is inside p1
            return p2


        # Edge intersections

        if p1[1] <= p2[0]:
            if p1[1] == p2[0]:
                return [ p1[1], p1[1] ]
            else:
                return []

        if p2[1] <= p1[0]:
            if p2[1] == p1[0]:
                return [ p2[1], p2[1] ]
            else:
                return []


        # Partial Intersections 

        if p1[1] > p2[0] and p1[1] < p2[1]: 
            return [p2[0], p1[1]]

        if p1[0] > p2[0] and p1[1] > p2[1]:
            return [p1[0], p2[1]]

        raise Exception('unhandled case: ', p1, p2)



    def find_intersections(self, points: List[List[int]], is_sorted=True) :

        num_baloons = len(points)
        
        # find and remove intersecting baloons
        if num_baloons == 0:
            return {}
        
        if num_baloons == 1:
            return {0:set()}

        # check points axis are sorted 
        for p in points:
            p0 = p[0]
            p1 = p[1]
            if p1 < p0:
                raise Exception('error.')


        #print('points', points)

        point_inter_points = {}
       
        for i in range(0, num_baloons):
            p1 = points[i]
            if i not in point_inter_points:
                point_inter_points[i] = set[int]()
                  
            for k in range(i+1, num_baloons):
                p2 = points[k]
                if is_sorted and p2[0] > p1[1]: # sorting allows to not look at larger points that cannot have intersections
                    break

                ir = self.get_intersecting_range(p1, p2)
                
                if len(ir) > 0:
                    # print(i,k,p1, p2, ir, point_inter_points)
                    # input()
                    point_inter_points[i].add(k)
                    if k in point_inter_points:
                        point_inter_points[k].add(i)
                    else:
                        point_inter_points[k] = set([i])
                    

        # print(point_inter_points)
        # input()

        return point_inter_points



    def trim_singles_double(self, pvp):

        num_arrows = 0

        while True:
            pilen = []
            for i in pvp.keys():
                if pvp[i] is not None:
                    pilen.append([i, len(pvp[i])])

            # sort by num of intersections asc
            pilen.sort(key=lambda p: (p[1]))

            #print(pilen)
            if len(pilen) == 0:
                return num_arrows

            if pilen[0][1] > 1: # no singles or doubles
                return num_arrows

            for p in pilen:
                if p[1] == 0: # points with no intersections
                    if p[0] in pvp:
                        num_arrows += 1
                        pvp.pop(p[0])

                if p[1] == 1: # single intersection with another point, remove both.
                    
                    if p[0] in pvp:
                        num_arrows += 1
                        pneighs = pvp[p[0]]
                        self.remove_p(p[0], pvp)
                        for neigh in pneighs:
                            self.remove_p(neigh, pvp)

                        # now find and remove if any other elemented intersected with it. 

                if p[1] > 1:
                    break


    def remove_p(self, pi, pvp):

        if pi in pvp:
            piset = pvp.pop(pi)

            for p in piset:
                if p in pvp:
                    pneighset = pvp[p]
                    if pneighset is not None:
                        pneighset.remove(pi)



    def remove_most_occuring(self, pvp, points):

        num_arrows = 0
        pilen = []
        for i in pvp.keys():
            if pvp[i] is not None:
                pilen.append([i, len(pvp[i])])

        # sort by num of intersections desc 
        pilen.sort(key=lambda p: (-p[1]))

        #print(pilen)
        if len(pilen) == 0:
            return num_arrows

        mostpi = pilen[0][0]
        most_pi_point = points[mostpi]
        #mostpset = pvp.pop(mostpi)
        mostpset = pvp[mostpi]
        print('mostpi', mostpi, mostpset)

        # find most common range, and only remove based on this range.

        common_ranges = []
        for pi in mostpset:
            pi_point = points[pi]

            for pi2 in mostpset:
                pi_point2 = points[pi2]

                inter = self.get_intersecting_range(pi_point2, pi_point)
                common_ranges.append(inter)


        # try permutations on ranges 

        longest_range_span = 0
        longest_range = []
        for ri in range(0, len(common_ranges)):
            
            range_span = 0
            for pi in mostpset:
                pi_point = points[pi]
                
                if len(common_ranges[ri]) > 0:
                    inter = self.get_intersecting_range(common_ranges[ri], pi_point)
                    if len(inter) > 0:
                        range_span += 1

            if range_span > longest_range_span:
                longest_range_span = range_span
                longest_range = common_ranges[ri]
             

        print(longest_range)
        
        if len(longest_range) == 0:
            return 0

        # find all points in this range
        shortest_range = longest_range
        for pi in mostpset:
            pi_point = points[pi]

            inter = self.get_intersecting_range(shortest_range, pi_point)
            if len(inter) > 0:
                shortest_range = inter

        
        points_to_remove = []
        for pi in mostpset:
            pi_point = points[pi]

            if len(self.get_intersecting_range( [shortest_range[0], shortest_range[0] ], pi_point)) > 0:
                points_to_remove.append(pi)
                
                
        for pi in points_to_remove:   
            self.remove_p(pi, pvp)


      
        return 1


    def super_simple(self, points: List[List[int]]) -> int:



        working_points = points

        num_arrows = len(working_points) 

        if num_arrows == 0:
            return 0

        if num_arrows == 1:
            return 1


        working_points.sort(key=lambda p: (p[0], p[1]))


        starting_baloon = working_points[0]

        for i in range(1, len(points)):
            current_baloon = points[i]

            inter = self.get_intersecting_range(starting_baloon, current_baloon)
            if len(inter) > 0:
                num_arrows -= 1
                starting_baloon = inter 
            else:
                starting_baloon = current_baloon


        return num_arrows




    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        return self.super_simple(points=points)






s = Solution()

out = s.findMinArrowShots(points=
   [[11702305,96123230],[37477084,64813411],[72660336,131786841],[5750846,38372575],[661313,34587170],[41616124,125970019],[39819582,40920127],[98898814,147132181],[10515434,96505798],[74344043,134657793]]
    )

print(out)




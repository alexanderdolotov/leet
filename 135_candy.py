
from typing import List

'''

135. Candy
Hard

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

 

Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104


'''



class Solution:

    def need_candy(self, ratings: List[int], candies: List[int], idx: int) -> int:
        # returns max candy of neighbors with lower rating
        my_candy = candies[idx]
        my_rating = ratings[idx]

        if idx == 0 and ratings[1] < my_rating and candies[1] >= my_candy:
            return candies[1] - my_candy + 1

        if idx == len(ratings)-1 and ratings[idx-1] < my_rating and candies[idx-1] >= my_candy:
            return candies[idx-1] - my_candy + 1

        # middle case
        if idx > 0 and idx < len(ratings)-1:
            diff1 = 0
            diff2 = 0
            if ratings[idx-1] < my_rating and candies[idx-1] >= my_candy:
                diff1 = candies[idx-1] - my_candy + 1

            if ratings[idx+1] < my_rating and candies[idx+1] >= my_candy:
                diff2 = candies[idx+1] - my_candy + 1

            return max(diff1, diff2)

        return 0 # no lower neighbor
        

    def get_total_candies(self, candies: List[int]) -> int:
        total_candies = 0
        for i in range(0, len(candies)):
            total_candies +=candies[i] 

        return total_candies


    def add_incremental_candies(self, candies, start_idx, end_idx, increment=1):

        if increment > 0:
            running_inc = 0
        else:
            running_inc = end_idx-start_idx

        for i in range(start_idx, end_idx+1):
            if running_inc >= 0:
                candies[i] += running_inc
                running_inc += increment


    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)

        if n == 1:
            return 1

        if n == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3

        candies = [1]*n

        # find monotonic paths
        is_mono_asc = False 
        is_mono_desc = False
        mono_start_idx = -1
        prev_rating = ratings[0]
        curr_rating = ratings[1]

        if curr_rating > prev_rating:
            is_mono_asc = True 
            mono_start_idx = 0
        elif curr_rating < prev_rating:
            is_mono_desc = True
            mono_start_idx = 0

        for i in range(2, n):
            prev_rating = curr_rating 
            curr_rating = ratings[i]

            # if in ascending mode
            if is_mono_asc:
                if curr_rating <= prev_rating: # if rating not mono incremented
                    is_mono_asc = False 
                    # update from start of mono until now candies in incremental order:
                    self.add_incremental_candies(candies=candies, start_idx=mono_start_idx, end_idx=i-1, increment=1)

            if is_mono_desc:
                if curr_rating >= prev_rating: # if rating not mono incremented
                    is_mono_desc = False 
                    # update from start of mono until now candies in incremental order:
                    self.add_incremental_candies(candies=candies, start_idx=mono_start_idx, end_idx=i-1, increment=-1)


            if not is_mono_asc and curr_rating > prev_rating:
                is_mono_asc = True 
                mono_start_idx = i 

            if not is_mono_desc and curr_rating < prev_rating:
                is_mono_desc = True 
                mono_start_idx = i

        # if finished in mono state
        if is_mono_asc:
            self.add_incremental_candies(candies=candies, start_idx=mono_start_idx, end_idx=n-1, increment=1)
        elif is_mono_desc:
            self.add_incremental_candies(candies=candies, start_idx=mono_start_idx, end_idx=n-1, increment=-1)
            
        #print('mono candies', candies)

        candy_added = True
        while candy_added:

            candy_added = False
            for i in range(0, n):
                candy_to_add = self.need_candy(ratings=ratings, candies=candies, idx=i)
                
                if candy_to_add > 0:
                    candies[i] += candy_to_add
                    candy_added = True

            #print('candies: ', candies)

            #print('total candies: ', self.get_total_candies(candies))
        
        return self.get_total_candies(candies)



s = Solution()
out = s.candy(ratings=[1,2,2 ])
print(out)


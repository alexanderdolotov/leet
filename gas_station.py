
from typing import List


'''
134. Gas Station
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.


Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

 

Constraints:

    n == gas.length == cost.length
    1 <= n <= 105
    0 <= gas[i], cost[i] <= 104
    The input is generated such that the answer is unique.

 '''


class Solution:

    def n2_sol(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)

        starting_index, lowest_milage = self.get_lowest_milage_idx(gas, cost)
        print('starting_index: ', starting_index)
        for i in range(0,l): 

            # go backwards from starting index, which is the highest milage index
            gas_idx1 = (starting_index+i+1) % l
            
            if gas[gas_idx1] < cost[gas_idx1]:
                continue
            if gas[gas_idx1] == 0:
                continue
            if gas[gas_idx1] <= cost[gas_idx1] and lowest_milage < 0:
                continue

            print('gas_idx1: ', gas_idx1)
            car_gas = 0
            for j in range(0,l):
                gas_idx2 = (gas_idx1+j) % l
                car_gas += gas[gas_idx2] - cost[gas_idx2]
                if car_gas < 0:
                    break
                
           
            if car_gas >= 0:
                return gas_idx1
                
        return -1


    def n_sol(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)

        starting_index = self.get_lowest_milage_idx(gas, cost)
        print('starting_index: ', starting_index)
        gas_idx1 = starting_index + 1

        # find next positive milage index
        for i in range(0,l):
            gas_idx2 = (gas_idx1+i) % l
            if gas[gas_idx2] - cost[gas_idx2] > 0:
                gas_idx1 = gas_idx2
                break

        print('gas_idx1: ', gas_idx1)
        car_gas = 0
        for j in range(0,l):
            gas_idx2 = (gas_idx1+j) % l
            car_gas += gas[gas_idx2] - cost[gas_idx2]
            if car_gas < 0:
                return -1

        return gas_idx1


    def get_highest_milage_idx(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        highest_milage = 0
        highest_milage_idx = -1
        for i in range(0,l):
            if gas[i] - cost[i] >= highest_milage:
                highest_milage = gas[i] - cost[i]
                highest_milage_idx = i
        return highest_milage_idx


    def get_lowest_milage_idx(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        lowest_milage = 0
        lowest_milage_idx = -1
        for i in range(0,l):
            if gas[i] - cost[i] <= lowest_milage:
                lowest_milage = gas[i] - cost[i]
                lowest_milage_idx = i
        return lowest_milage_idx, lowest_milage

   
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        return self.n2_sol(gas, cost)



s = Solution()
out = s.canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2])
print(out)


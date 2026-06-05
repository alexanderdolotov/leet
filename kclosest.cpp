// https://leetcode.com/problems/k-closest-points-to-origin/

#include <queue>
#include <vector>
#include <functional>  // for std::greater
#include <unordered_map>


class Solution {
public:
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        
        std::priority_queue<int> pq;
        std::unordered_map<int, std::vector<std::vector<int>>> pqmap;

        for(std::vector<int> p :  points){
            int p0 = p[0];
            int p1 = p[1];
            int pc = -std::abs(p0*p0 + p1*p1);

            pq.push(pc);
            pqmap[pc].push_back(p);

        }

        std::vector<std::vector<int>> result = std::vector<std::vector<int>>(k);
        int points_added = 0;
        while(points_added < k){

            int dist = pq.top();
            pq.pop();

            std::vector<std::vector<int>> points = pqmap[dist];
            

            for(std::vector<int> point : points){
                if (points_added >= k){
                    return result;
                }

                result[points_added] = point;
                points_added++;
            }

        }

        return result;
       
    }
};
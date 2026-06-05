// https://leetcode.com/problems/combination-sum/
/*

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the

of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40


*/


#include <vector>
#include <iostream>
#include <unordered_set> 
#include <unordered_map>
#include <cmath> 

using namespace std;


class Solution {

    public:
        
        std::unordered_map<int, vector<vector<int>>> target_maps;

        void printvec(vector<int> v){

            cout << "{";
            for (int i : v){
                cout << " " << i;
            }
            cout << " }" << endl;

        }


        // inputs sorted in ascending order candidates
        vector<vector<int>> r_combinations(vector<int> candidates, int target){

            vector<vector<int>> combinations;

            if (target <= 0){
                return combinations;
            }

            if(this->target_maps.count(target)){
                return target_maps[target];
            }
            
            for(int i : candidates){

                if (i > target){
                    break;
                }

                //cout << "cadidate: " << i << " target: " << target << endl;
                int nothing;
                //std::cin >> nothing;

                int sum_combo = 0;
                vector<int> combo_attempt = vector<int>();
                while(sum_combo <= target){

                    sum_combo += i;

                    if (sum_combo > target){
                        break;
                    }

                    combo_attempt.push_back(i);

                    if (sum_combo == target){

                        combinations.push_back(combo_attempt);
                        vector<int> combo_attempt = vector<int>();
                        combo_attempt.push_back(i);
                    }

                    int new_target = target - i;
                    if (new_target > 0){
                        vector<vector<int>> combo_differences = r_combinations(candidates, target - i);

                        for(vector<int> combo_diff : combo_differences){

                            combo_diff.push_back(i);
                            combinations.push_back(combo_diff);

                        }

                    } else {
                        break;
                    }

                }


            } // i

        
        vector<vector<int>> combinations_unique;
        unordered_set<int> combohashes;
        for(vector<int> combo :  combinations){

            float combohash = 1;
            for(int i : combo){
               // combohash += (int)( sqrt(i * i * i)*10000 );
               combohash += (1 << i*i);
            }

            if(!combohashes.count(combohash)){
                combinations_unique.push_back(combo);
                combohashes.insert(combohash);
            }
        }


        target_maps[target] = combinations_unique;

        return combinations_unique;
    } // r_combinations


public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {   
       
        // sort in ascending
        std::sort(candidates.begin(), candidates.end());

        vector<vector<int>> combinations = r_combinations(candidates, target);

        return combinations;
    }
};


//  g++ -std=c++11 combsum.cpp -o combsum && ./combsum
int main() {
   
    vector<int> candidates = {4,2,7,5,6};

    int target = 16;

    Solution sol;
    vector<vector<int>> combinations = sol.combinationSum(candidates, target);

    cout << "total combinations: " << combinations.size() << endl;
    for ( auto combo : combinations){

        cout << "{";
        int combo_sum = 0;
        float combo_hash = 0;
        for (int i : combo){
            cout << " " << i;
            combo_sum += i;
            combo_hash += (int)( sqrt(i * i * i)*1000 );
        }
        cout << " } combo hash: " << combo_hash << endl;

    }


    return 0;
}
/*
[4, 4, 4, 4]
[4, 4, 4, 2, 2]
[4, 4, 2, 2, 2, 2]
[4, 4, 2, 6]
[4, 2, 2, 2, 2, 2, 2]
[4, 2, 2, 2, 6]
[4, 2, 5, 5]
[4, 7, 5]
[4, 6, 6]
[2, 2, 2, 2, 2, 2, 2, 2]
[2, 2, 2, 2, 2, 6]
[2, 2, 2, 5, 5]
[2, 2, 7, 5]
[2, 2, 6, 6]
[2, 7, 7]
[5, 5, 6]
*/

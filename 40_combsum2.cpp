

#include <vector>
#include <unordered_set> 
#include <unordered_map>
#include <cmath> 

using namespace std;

class Solution {

private:
    unordered_map<int, vector<vector<int>>> target_maps;
    int MAX_LEN = 40;

    bool compare_vec_signs(vector<int>& vec1, vector<int>& vec2){

        for(int i =0; i < MAX_LEN; i++){

            if(vec1[i] != vec2[i]){
                return false;
            }

        }

        return true;

    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        vector<vector<int>> combinations;
        vector<vector<int>> combos_signs;

        if(this->target_maps.count(target)){
            return target_maps[target];
        }

        if (target <= 1){
            return combinations;
        }

        
        for(int i : candidates){
    
            // if (i > target){break;} // if sorted

            if (i > target){continue;}
            if (i == target){
                combinations.push_back({i});
            } else {
                int new_target = target - i;
                if (new_target > 1){
                    vector<vector<int>> combo_differences = combinationSum(candidates, new_target);
                    for(vector<int> combo_diff : combo_differences){

                        combo_diff.push_back(i);

                        vector<int> combo_sign = vector<int>(MAX_LEN, 0);
                        for(int j : combo_diff){
                            combo_sign[j] += 1;
                        }

                        bool found_combo = false;
                        for(vector<int> sign : combos_signs){
                            if (compare_vec_signs(sign, combo_sign)){
                                found_combo = true;
                                break;
                            }
                        }

                        
                        if(!found_combo){
                            combos_signs.push_back(combo_sign);
                            combinations.push_back(combo_diff);
                        }
                        

                    }


                } 

            }

            
        }

       
        target_maps[target] = combinations;
        return combinations;
    }
};


#include <iostream>
//  g++ -std=c++11 combsum2.cpp -o combsum2 && ./combsum2
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
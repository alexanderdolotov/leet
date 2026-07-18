using namespace std;


class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        
        std::vector<std::vector<int>> intervals = std::vector<std::vector<int>> (nums.size());
        for(int i=0; i < nums.size(); i++){
            intervals[i] = {i, nums[i]};
        }

        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) { 
           return a[1] < b[1];
        });

        int i = 0;
        int k = nums.size()-1;
        while(true){

            int sum = intervals[i][1] + intervals[k][1];

            std::cout << "sum: " << sum << " i: " << intervals[i][1] << " k: " << intervals[k][1] << endl;
            
            if (sum == target){
                return {intervals[i][0], intervals[k][0]};
            } else if (sum < target){
                i++;
            } else {
                k--;
            }

        }
        
    }
};
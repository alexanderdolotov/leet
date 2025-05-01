// https://leetcode.com/problems/median-of-two-sorted-arrays/
//  g++ -std=c++11 medians.cpp -o medians && ./medians

#include <iostream>
#include <vector>


double findMedian(std::vector<int>& nums, int start=0, int end=1){

    int numslen = (end - start);
    int m1 = (numslen / 2) + start;
  
    if (numslen % 2 == 0){
        return ( nums[m1] + nums[m1-1] ) / 2.0; 
    } else {
        return nums[m1];
    }

}



int findLowerMedian(std::vector<int>& nums, int start=0, int end=1){

    int numslen = (end - start);
    int m1 = (numslen / 2) + start;

    if (numslen % 2 == 0){
        return nums[m1-1]; 
    } else {
        return nums[m1];
    }


}


double binary_search_closest(std::vector<int>& nums, int val){

    int len = nums.size();

    if (len < 2){
        return 0;
    }

    int middle = len / 2;
    int size = middle / 2;
    int attempt = 0;

    while(true){

        if(attempt > 3){
            return middle;
        }

        if(middle >= len){
           return len;
        }

        if(middle < 0){
            return -1;
        }

        int mval = nums[middle];
        //std::cout << middle << " mavl:" << mval << " val: " << val << std::endl;

        if (mval == val){
            return middle;
        }

        if(mval > val){
            middle = middle - size;
        } else {
            middle = middle + size;
        }

        size = size / 2;

        if (size < 1){
            size = 1;
            attempt++;
        }
    }

    return middle;
}



double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {     

    int nums1_start = 0;
    int nums1_end = nums1.size();

    int nums2_start = 0;
    int nums2_end = nums2.size();

    while(true){

        if(nums1_start < 0){
            nums1_start = 0;
        }

        if(nums2_start < 0){
            nums2_start = 0;
        }

        if(nums1_end > nums1.size()){
            nums1_end = nums1.size();
        }

        if(nums2_end > nums2.size()){
            nums2_end = nums2.size();
        }

        int lmedian1 = findLowerMedian(nums1, nums1_start, nums1_end);
        int lmedian2 = findLowerMedian(nums2, nums2_start, nums2_end);
    
        std::cout << "lmedian1: " << lmedian1 << std::endl;
        std::cout << "lmedian2: " << lmedian2 << std::endl;
    
        int idx1 = binary_search_closest(nums1, lmedian2);
        int idx2 = binary_search_closest(nums2, lmedian1);
    
        std::cout << "idx1: " << idx1 << std::endl;
        std::cout << "idx2: " << idx2 << std::endl;

        int nums1_new_start = idx1;
        int nums1_new_end = (nums2_end - nums2_start) / 2 + nums2_start;

        int nums2_new_start = idx2;
        int nums2_new_end = (nums1_end - nums1_start) / 2 + nums1_start;

        nums1_start = nums1_new_start;
        nums1_end = nums1_new_end;

        nums2_start = nums2_new_start;
        nums2_end = nums2_new_end;

        int x;
        std::cin >> x;

    }
   



    return 0;
}




int main() {
    std::cout << "Starting Script" << std::endl;

    std::vector<int> vec1 = {1,2,3,4,5,6,7,8,9};
    std::vector<int> vec2 = {2,4,8,16,32,64,128,256,512,1024,2048,2049,2050,2051};

    findMedianSortedArrays(vec1, vec2);

    return 0;
}







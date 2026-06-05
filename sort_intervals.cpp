// https://leetcode.com/problems/merge-intervals/


#include <vector>
#include <functional>

template <typename T>
class MergeSort {
public:
    explicit MergeSort(std::function<bool(const T&, const T&)> compareFunc) : compare(compareFunc) {}
    // TODO implement the following functions in ../src/MergeSort.cpp
    void sort(std::vector<T>& arr);

private:
    std::function<bool(const T&, const T&)> compare;
    void merge(std::vector<T>& arr, const std::vector<T>& left, const std::vector<T>& right);
};



template <typename T>
void MergeSort<T>::sort(std::vector<T>& arr){

    size_t size = arr.size();
    if(size <= 1){
        return;
    } else if (size == 2){

        T v1 = arr[0];
        T v2 = arr[1];

        // if v1 compares to v2, preserve array
        if(compare(v1, v2)){
            return;
        } else {
            // otherwise, switch places
            arr[0] = v2;
            arr[1] = v1;
        }

    } else {

        size_t left_size = size / 2;
        std::vector<T> arr_left = std::vector<T>(left_size);
        std::vector<T> arr_right = std::vector<T>(size-left_size);

        for(size_t i = 0; i < left_size; i++){
            arr_left[i] = (arr[i]);
        }

        for(size_t i = left_size; i < size; i++){
            arr_right[i-left_size] = (arr[i]);
        }
      
        sort(arr_left);
        sort(arr_right);
        merge(arr, arr_left, arr_right);

    }

}

template <typename T>
void MergeSort<T>::merge(std::vector<T>& arr, const std::vector<T>& left, const std::vector<T>& right){

    size_t size = arr.size();
    size_t left_size = left.size();
    size_t right_size = right.size();

    size_t lefti = 0;
    size_t righti = 0;
    for(size_t i=0; i < size; i++){

        if ( lefti < left_size && righti < right_size ){

            if( compare(left[lefti], right[righti]) ){
                arr[i] = left[lefti];
                lefti++;
            } else {
                arr[i] = right[righti];
                righti++;
            }

        } else {

            if (lefti < left_size){
                arr[i] = left[lefti];
                lefti++;
            }

            if(righti < right_size){
                arr[i] = right[righti];
                righti++;
            }

        }

    }

}


class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        
        MergeSort<std::vector<int>> rangeSort([](const std::vector<int>& a, const std::vector<int>& b) { 
            if (a[0] == b[0]){
                return a[1] < b[1];
            } else {
                return a[0] < b[0]; 
            }
            
        });

        rangeSort.sort(intervals);

        std::vector<std::vector<int>> merged_ranges = std::vector<std::vector<int>>();

        int range_start = intervals[0][0];
        int range_end = intervals[0][1];
        for(int i=0; i < intervals.size()-1; i++){

            if(intervals[i+1][0] <= range_end ){

                if (intervals[i+1][1] > range_end){
                    range_end = intervals[i+1][1]; 
                }
                

            } else {
                merged_ranges.push_back({range_start, range_end});
                range_start = intervals[i+1][0];
                range_end = intervals[i+1][1];
            }

        }

        merged_ranges.push_back({range_start, range_end});

        return merged_ranges;

    }
};



#include <iostream>
#include <vector>

int binarySearch(std::vector<int>& nums, int target){
    int left = nums.begin();
    int right = nums.end() - 1;
    
    while(left<=right){
        auto mid = left + (right-left)/2;
        if(*mid == target){
            return mid;
        }else if (*mid<target){
            left = mid+1;
        }else{
            right = mid-1;
        }
    }
    
    
    return -1;
}

int main() {
    
    int arr[] = {0,4,5,7,11};
    
    int pos = binarySearch(arr,11);
    std::cout << pos << std::endl;
    return 0;
}

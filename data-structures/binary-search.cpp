#include <iostream>

int binarySearch(int a[], int target){
    int left = 0;
    int right = sizeof(a[0]);
    
    while(left<=right){
        int piv = (right+left) / 2;
        if(a[piv]==target){
            return piv;
        }else{
            if(target<a[piv]){
                right = piv - 1;
            }else{
                left = piv + 1;
            }
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

#include <iostream>
#include "bubble_sort.h"
#include "insertion_sort.h"
#include "selection_sort.h"
#include "quick_sort.h"
#include "merge_sort.h"
#include "heap_sort.h"

int main() {
    int n;
    std::cin >> n;
    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
   bubbleSort(arr,n);
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
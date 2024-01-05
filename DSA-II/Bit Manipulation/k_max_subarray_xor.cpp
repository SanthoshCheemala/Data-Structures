#include <iostream>
#include <vector>
using namespace std;

int findMaximumXOR(vector<int>& nums) {
    int maxXOR = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        int currXOR = 0;
        for (int j = i; j < n; ++j) {
            currXOR ^= nums[j];
            maxXOR = max(maxXOR, currXOR);
        }
    }
    return maxXOR;
}

int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    
    vector<int> arr(n);
    cout << "Enter the elements of the array:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int maxXOR = findMaximumXOR(arr);
    cout << "Maximum subarray XOR value: " << maxXOR << endl;
    return 0;
} 
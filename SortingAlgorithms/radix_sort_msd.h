#include <iostream>
#include <vector>

const int RANGE = 10;

int get_max_digits(const std::vector<int>& arr) {
    int max_digits = 0;
    for (int num : arr) {
        int curr_digits = 0;
        int temp = num;
        if (temp == 0) {
            curr_digits = 1;
        }
        else {
            while (temp != 0) {
                temp /= 10;
                curr_digits++;
            }
        }

        if (curr_digits > max_digits) {
            max_digits = curr_digits;
        }
    }
    return max_digits;
}

void countingSort(std::vector<int>& arr, int exp) {
    std::vector<int> count(RANGE, 0);
    std::vector<int> output(arr.size(), 0);

    for (int num : arr) {
        int digit = (num / exp) % RANGE;
        count[digit]++;
    }

    for (int i = 1; i < RANGE; i++) {
        count[i] += count[i - 1];
    }

    for (int i = arr.size() - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % RANGE;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    for (int i = 0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
}

void radixSortMSD(std::vector<int>& arr) {
    int max_digits = get_max_digits(arr);
    int exp = 1;

    for (int i = 0; i < max_digits; i++) {
        countingSort(arr, exp);
        exp *= 10;
    }
}
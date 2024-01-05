#include <iostream>

int get_max(int* arr, int size) {
	int max = arr[0];
	for (int i = 0; i < size; i++) {
		if (arr[i] > max) max = arr[i];
	}

	return max;
}

void countingSort(int* arr, int size, int exp) {
	const int RANGE = 10;
	int* count = new int[RANGE];
	int* output = new int[size];

	for (int i = 0; i < RANGE; i++) {
		count[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		count[(arr[i] / exp) % RANGE]++;
	}

	for (int i = 1; i < RANGE; i++) {
		count[i] += count[i - 1];
	}

	for (int i = size - 1; i >= 0; i--) {
		output[count[(arr[i] / exp) % RANGE] - 1] = arr[i];
		count[(arr[i] / exp) % RANGE]--;
	}

	for (int i = 0; i < size; i++) {
		arr[i] = output[i];
	}
}

void radixSortLSD(int* arr, int size) {
	int max = get_max(arr, size);

	for (int exp = 1; max / exp > 0; exp *= 10) {
		countingSort(arr, size, exp);
	}
}
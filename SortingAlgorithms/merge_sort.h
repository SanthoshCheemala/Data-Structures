#include <iostream>

void merge(int* arr, int* left, int left_size, int* right, int right_size) {
	int i = 0;		// Index for left sub-array 
	int j = 0;		// Index for right sub-array
	int k = 0;		// Index for merged array

	while (i < left_size && j < right_size) {
		if (left[i] <= right[j]) {
			arr[k] = left[i];
			i++;
		} else {
			arr[k] = right[j];
			j++;
		}
		k++;
	}

	while (i < left_size) {
		arr[k] = left[i];
		i++;
		k++;
	}

	while (j < right_size) {
		arr[k] = right[j];
		j++;
		k++;
	}
}

void mergeSort(int* arr, int size) {
	if (size <= 1) return;

	int mid = size / 2;

	int* left = new int[mid];
	int* right = new int[size - mid];

	for (int i = 0; i < mid; i++) {
		left[i] = arr[i];
	}

	for (int i = mid; i < size; i++) {
		right[i - mid] = arr[i];
	}

	mergeSort(left, mid);
	mergeSort(right, size - mid);

	merge(arr, left, mid, right, size - mid);
}
#include <iostream>

int partition(int* arr, int low, int high) {
	int pivot = arr[high];
	int i = low;

	for (int j = low; j < high; j++) {
		if (arr[j] < pivot) {
			std::swap(arr[i], arr[j]);
			i++;
		}
	}

	std::swap(arr[i + 1], arr[high]);

	return (i + 1);
}

void quickSort(int* arr, int low, int high) {
	if (low < high) {
		int pivotIndex = partition(arr, low, high);
		quickSort(arr, low, pivotIndex - 1);
		quickSort(arr, pivotIndex + 1, high);
	}
}
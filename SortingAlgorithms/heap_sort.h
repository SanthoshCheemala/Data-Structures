#include <iostream>

void heapify(int* arr, int n, int i) {
	int largest = i;
	int left_child = 2 * i + 1;
	int right_child = 2 * i + 2;

	if (left_child < n && arr[left_child] > arr[largest]) largest = left_child;

	if (right_child < n && arr[right_child] > arr[largest]) largest = right_child;

	if (largest != i) {
		std::swap(arr[i], arr[largest]);
		heapify(arr, n, largest);
	}
}

void heapSort(int* arr, int n) {
	for (int i = n / 2 - 1; i >= 0; i--) {
		heapify(arr, n, i);
	}

	for (int i = n - 1; i > 0; i--) {
		std::swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}
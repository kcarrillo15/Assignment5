import time
import random

numbers = [34, 7, 23, 32, 5, 62]

sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

def measure_time(sort_fn, arr):
    start_time = time.time()
    sort_fn(arr)
    end_time = time.time()
    return end_time - start_time

list_sizes = [1000, 10000, 100000]
for size in list_sizes:
    arr = random.sample(range(size * 2), size)
    
    sorted_time = measure_time(sorted, arr)

    merge_sort_time = measure_time(merge_sort, arr)

    print(f"List Size: {size}")
    print(f"Python's sorted() Time: {sorted_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
    print("-" * 30)

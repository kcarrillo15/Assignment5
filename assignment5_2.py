import time
import random
 
 #problem 2
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization: stops if the list is already sorted
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the list into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge sorted halves
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
    
    bubble_arr = arr.copy()
    bubble_time = measure_time(bubble_sort, bubble_arr)

    merge_arr = arr.copy()
    merge_time = measure_time(merge_sort, merge_arr)

    print(f"List Size: {size}")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print("-" * 30)


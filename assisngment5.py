import time
import random


#problem 1

# 1

def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1
# 2

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) //2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1
    
def measure_time(search_function, array, target):
    start = time.time()
    search_function(array, target)
    end = time.time()
    return end - start

list_sizes = [1000, 100000,100000 ]

for size in list_sizes:
    array = list(range(size))
    target = random.choice(array)
    linear_time = measure_time(linear_search, array, target)
    binary_time = measure_time(binary_search, array, target)
    
    print(f"List Size: {size}")
    print(f"Linear Search Time: {linear_time:.6f} seconds")
    print(f"Binary Search Time: {binary_time:.6f} seconds")
    print("-" * 30)
    
   
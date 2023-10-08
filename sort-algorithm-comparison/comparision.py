import random
import time

# Generate a random list of numbers
arr = [random.randint(0, 10000) for _ in range(1000)]

# Measure the execution time for Radix Sort
start_time = time.time()
radix_sort(arr.copy())
radix_sort_time = time.time() - start_time

# Measure the execution time for Quicksort
start_time = time.time()
quicksort(arr.copy())
quicksort_time = time.time() - start_time

print(f"Radix Sort Time: {radix_sort_time} seconds")
print(f"Quicksort Time: {quicksort_time} seconds")

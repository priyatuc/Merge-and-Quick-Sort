import random
import time
import tracemalloc

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 # find the midpoint of the array
    left = merge_sort(arr[:mid]) # recursively sort the left half
    right = merge_sort(arr[mid:]) # recursively sort the right half

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # compare elements from both halves
            result.append(left[i])  # add smaller element to result
            i += 1
        else:
            result.append(right[j]) # add smaller element to result
            j += 1
    result.extend(left[i:]) # add any remaining elements from left half
    result.extend(right[j:]) # add any remaining elements from right half
    return result

def measure_merge_sort(arr):
    tracemalloc.start()
    start_time = time.perf_counter()
    sorted_arr = merge_sort(arr)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024  # time in seconds, memory in KB

datasets = {
    "Random": random.sample(range(1, 10001), 10000), # generate a random array of 10,000 unique integers
    "Sorted": list(range(1, 10001)), # already sorted array
    "Reverse": list(range(10000, 0, -1)) # reverse sorted array
}

# Run experiments and store metrics
results = []
for name, data in datasets.items():
    time_taken, memory_used = measure_merge_sort(data)
    results.append((name, time_taken, memory_used))

# Print table
print(f"{'Dataset':<10} {'Time (s)':<10} {'Memory (KB)':<12}")
for name, time_taken, memory_used in results:
    print(f"{name:<10} {time_taken:<10.5f} {memory_used:<12.2f}")

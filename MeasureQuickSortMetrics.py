import random
import time
import tracemalloc

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_sort(func, arr):
    tracemalloc.start()
    start = time.perf_counter()
    sorted_arr = func(arr.copy())  
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024  

size = 10000
datasets = {
    "Random": random.sample(range(1, size+1), size),
    "Sorted": list(range(1, size+1)),
    "Reverse": list(range(size, 0, -1))
}

results = []

for name, data in datasets.items():
    quick_time, quick_mem = measure_sort(quick_sort, data)
    results.append((name, quick_time, quick_mem))

# Print Results Table
print(f"{'Dataset':<10} {'Time (s)':<10} {'Memory (KB)':<12}")
for r in results:
    print(f"{r[0]:<10} {r[1]:<10.5f} {r[2]:<12.2f}")

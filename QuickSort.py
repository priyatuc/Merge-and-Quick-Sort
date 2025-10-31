def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

array = [34, 7, 23, 32, 5, 62]
sorted_array = quick_sort(array)
print("Original array:", array)
print("Sorted array:", sorted_array)

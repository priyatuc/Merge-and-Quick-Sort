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

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)  # call the merge_sort function
print("Unsorted array:", arr)
print("Sorted array:", sorted_arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([29, 10, 14, 37, 14]))
print(selection_sort([5, 1, 4, 2, 8]))
print(selection_sort([64, 2]))

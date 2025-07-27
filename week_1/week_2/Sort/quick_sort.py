def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([10, 7, 8, 9, 1, 5]))
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
print(quick_sort([3, 7, 8, 5, 2, 1, 9, 5, 4]))

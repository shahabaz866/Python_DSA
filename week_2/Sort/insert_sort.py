# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# print(insertion_sort([12, 11, 13, 5, 6]))
# print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))
# print(insertion_sort([1, 2, 3, 4]))


# def insertion_sort(arr):
#     print(f"Original list: {arr}\n")
    
#     for i in range(1, len(arr)):
#         key = arr[i]      
#         j = i - 1
#         print(f"Step {i}: Trying to insert {key} into the sorted part {arr[:i]}")

#         while j >= 0 and key < arr[j]:
#             print(f"  {arr[j]} > {key} → shifting {arr[j]} to the right")
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key
#         print(f"  Inserted {key} at position {j + 1}")
#         print(f"  Current list: {arr}\n")
    
#     print(f"Sorted list: {arr}")
#     print("=" * 40 + "\n")
#     return arr

# print(insertion_sort([12, 11, 13, 5, 6]))
# print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))
# print(insertion_sort([1, 2, 3, 4]))


def insert_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        


if __name__ =='__main__':
    elements =[11,9,29,7,2,15,28]
    insert_sort(elements)
    print(elements)
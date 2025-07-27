# Python List Operations

# Creating a list
my_list = [10, 20, 30, 40, 50]

# Display the original list
print("Original List:", my_list)

# Accessing elements by index
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing the list
print("First 3 elements:", my_list[:3])

# Appending elements to the list
my_list.append(60)
print("After appending 60:", my_list)

# Inserting elements at a specific position
my_list.insert(2, 25)  
print("After inserting 25 at index 2:", my_list)

# Removing an element
my_list.remove(40)  
print("After removing 40:", my_list)

# Popping an element (removes last element by default)
removed_element = my_list.pop()
print(f"After popping element {removed_element}:", my_list)

# Finding an element's index
index = my_list.index(30) if 30 in my_list else -1
print("Index of 30:", index)

# Sorting the list
my_list.sort()
print("Sorted List:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed List:", my_list)

# Checking if an element exists
print("Is 20 in the list?", 20 in my_list)

# Length of the list
print("Length of list:", len(my_list))

# Iterating through the list
print("List elements:")
for item in my_list:
    print(item, end=" ")


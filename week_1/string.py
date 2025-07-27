# String operations in Python

# Taking user input
s = input("Enter a string: ")

# Display the original string
print("\nOriginal String:", s)

# String Length
print("Length of the string:", len(s))

# Accessing characters
print("First character:", s[0] if len(s) > 0 else "String is empty")

# Slicing
print("First 5 characters:", s[:5])

# Concatenation
s2 = " - Python Programming"
print("Concatenated String:", s + s2)

# Finding substring
sub = "Python"
position = s.find(sub)
if position != -1:
    print(f"'{sub}' found at index {position}")
else:
    print(f"'{sub}' not found in the string")

# Replacing substring
print("String after replacement:", s.replace("Python", "Django"))

# Converting to uppercase and lowercase
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Splitting the string
words = s.split()
print("Words in the string:", words)

# Reversing the string

print("Reversed String:", s[::-1])

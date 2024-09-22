# Classwork 1: Basic List Operations

# 1. Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".

# 2. Print the entire list.

# 3. Access and print the first and last items in the list.

# 4. Add a new fruit "fig" to the list.

# 5. Remove "banana" from the list.

# 6. Change the value of the second item to "blueberry".

# 7. Print the length of the list.

fruit = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruit)

print("First item:", fruit[0])
print("Last item:", fruit[-1])

fruit.append("fig")

fruit.remove("banana")

fruit[1] = "blueberry"

print("Length of the list:", len(fruit))
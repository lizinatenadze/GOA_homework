# Classwork 3: Slicing and List Comprehensions
# Create a list named numbers that contains the integers from 1 to 10.
# Use list slicing to create a new list named first_half that contains the first five elements from numbers.
# Use list slicing to create another list named second_half that contains the last five elements from numbers.
# Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.
# Print all three lists: first_half, second_half, and squares.

number = list(range(1, 11))

first_half = number[:5]

second_half = number[5:]

squares = [x**2 for x in number]



print("First :", first_half)
print("Second :", second_half)
print("Squares:", squares)





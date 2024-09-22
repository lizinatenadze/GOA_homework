# Classwork 4: List Manipulation and Aggregation
# Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].
# Calculate and print the highest temperature using the max() function.
# Calculate and print the lowest temperature using the min() function.
# Calculate and print the average temperature using the sum() function divided by the length of the list.
# Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.
# Print the above_70 list.

temperatures = [72, 68, 75, 70, 78, 74, 71]


highest_temp = max(temperatures)
print("Highest temperature:", highest_temp)


lowest_temp = min(temperatures)
print("Lowest temperature:", lowest_temp)


average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)


above_70 = [temp for temp in temperatures if temp > 70]


print("Temperatures above 70 degrees:", above_70)
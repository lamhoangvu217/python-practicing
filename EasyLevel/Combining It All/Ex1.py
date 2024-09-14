# Write a program that takes a list of numbers as input and calculates the sum, product, and average of the numbers. 
# Use loops to perform the calculations.

# Explain in detail
# Calculates the sum of the numbers: The program should add up all the numbers in the list.
# Calculates the product of the numbers: The program should multiply all the numbers together.
# Calculates the average of the numbers: The program should find the mean (average) by dividing the sum of the numbers by the count of numbers in the list.
# Use loops for calculations: The sum, product, and average should be calculated using loops instead of built-in Python functions like sum() or prod().

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
sum = 0
product = 1
average = 0
for x in numbers:
    sum += x
    product *= x
average = sum / len(numbers)
print(sum, product, average)
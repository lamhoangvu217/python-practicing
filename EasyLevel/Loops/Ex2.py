# Write a program that takes a number as input and prints the multiplication table for that number (up to 10).
number = int(input("Enter a number: "))
for x in range(1, 11):
    print(f"{number} * {x} = {number * x}")
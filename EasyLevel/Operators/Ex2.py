# Write a program that calculates the area of a circle. The user should input the radius, and the program should use the formula: Area = π * r^2 (Use math.pi for π).
import math
r = float(input("Enter radius:"))
result = math.pi * r**2
print(result)
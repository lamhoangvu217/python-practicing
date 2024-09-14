# Create a program that calculates the factorial of a number (e.g., 5! = 5 × 4 × 3 × 2 × 1). Implement it using both a for loop and a while loop.
number = int(input("Enter a number: "))
result = 1
i = number

# for loop
for x in range(1, number + 1): # 3: 3 * 2 * 1 = 6
    result = result * x
# result = 1 * 1 = 1 -> result = 1 * 2 = 2 -> result = 2 * 3 = 6 
print(result)
    
# while loop

while i > 0:
    result *= i
    i -= 1
print(result)
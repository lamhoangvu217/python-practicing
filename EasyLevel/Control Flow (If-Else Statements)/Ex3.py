# Build a program that asks for a year and checks if it’s a leap year. A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("Its not a leap year")
# - Create a grading system that takes a score as input (0 to 100) and prints the corresponding grade:
#   - 90+ -> A
#   - 80-89 -> B
#   - 70-79 -> C
#   - 60-69 -> D
#   - Below 60 -> F

score = int(input("Enter a score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
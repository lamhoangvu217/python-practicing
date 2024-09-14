# Find the largest and smallest number in a list without using the min() or max() functions.
lists = [1, 5, 3, 9, 2, 6]
min = lists[0]
max = 0
for i in lists:
    if i > max:
        max = i
    if i < min:
        min = i
print(max, min)
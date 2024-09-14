# Flatten Nested Structures: Write a function that takes a nested list (a list of lists) and flattens it into a single list.

# using recursive
# input = [1, [2, 3], [4, [5, 6]], 7]
# output = [1, 2, 3, 4, 5, 6, 7]

lists = [1, [2, 3], [4, [5, 6]], 7]
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list): # base case:
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list
print(flatten_list(lists))
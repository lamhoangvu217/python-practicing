# Dictionary to List of Tuples: Write a function that converts a dictionary into a list of tuples, 
# where each tuple is a key-value pair from the dictionary.

# input: first_dict = {"name": "John", "age": 21, "major": "Computer Science"},
# output: result_tuple = [ ("name", "John"), ("age", 21), ("major", "Computer Science")]

first_dict = {"name": "John", "age": 21, "major": "Computer Science"}
x = list(first_dict.items())
print(x)
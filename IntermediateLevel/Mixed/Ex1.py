# Group By Key: Write a function that takes a list of dictionaries and groups them by a specified key. 
# For example, given a list of dictionaries with a "category" key, group the dictionaries by their category.
from collections import defaultdict

def groupDictionary(listOfDict, key):
    grouped_data = defaultdict(list)
    for item in listOfDict:
        grouped_data[item[key]].append(item)
    return dict(grouped_data)

students = [ 
    {"name": "John", "age": 21, "major": "Computer Science"},
    {"name": "Jane", "age": 22, "major": "Mathematics"},
    {"name": "Tom", "age": 23, "major": "Computer Science"},
    {"name": "Lucy", "age": 21, "major": "Mathematics"},
    {"name": "Mark", "age": 24, "major": "Physics"},
]

# output = {
#     "Computer Science": [
#        {"name": "John", "age": 21, "major": "Computer Science"},
#        {"name": "Tom", "age": 23, "major": "Computer Science"},
#     ],
#     "Mathematics": [
#         {"name": "Jane", "age": 22, "major": "Mathematics"},
#         {"name": "Lucy", "age": 21, "major": "Mathematics"},
#     ],
#     "Physics": [
#         {"name": "Mark", "age": 24, "major": "Physics"},
#     ]
# }
print(groupDictionary(students, "major"))
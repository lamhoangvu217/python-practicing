# Count Frequencies: Write a function that takes a list of elements 
# and returns a dictionary where the keys are the elements and the values are the counts of each element.
import operator
def dictionaryRender(lists):
    # Khởi tạo một dictionary rỗng
    count_dict = {}
    # Duyệt qua từng phần tử trong mảng
    for item in lists:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    # Lấy ra phần tử xuất hiện nhiều nhất
    maxValue = max(count_dict, key=count_dict.get)
    print(maxValue, count_dict)

lists = [2,3,1,2,3,2,5,6,7]
dictionaryRender(lists)
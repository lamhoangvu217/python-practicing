class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return f"Node({self.data})"
    def __repr__(self) -> str:
        return f"Node(data={self.data}, next={repr(self.next)})"
class NumberList:
    def __init__(self) -> None:
        self.head = None
    def append(self, number):
        new_num = Node(number)
        if self.head is None:
            self.head = new_num
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_num
    def display(self):
        current_node = self.head
        if current_node is None:
            print("Number list is empty")
        else:
            print("Your number list:")
            print("[", end="")
            while current_node:
                print(current_node.data, end="")
                if current_node.next:
                    print(", ", end="")
                current_node = current_node.next
            print("]")
    def sortList(self):
        current_node = self.head
def main():
    numberList = NumberList()
    while True: 
        print("\n=== Quản lý number list ===")
        print("1. Thêm số vào dãy")
        print("2. Hiển thị dãy số")
        print("3. Xóa số khỏi dãy")
        print("4. Sắp xếp dãy số tăng dần")
        choice = input("Chọn chức năng (1-4): ")
        if choice == "1":
            number = input("Nhập số: ")
            numberList.append(number)
            print(f"Đã thêm số '{number}' vào danh sách.")
        elif choice == "2":
            numberList.display()
if __name__ == "__main__":
    main()
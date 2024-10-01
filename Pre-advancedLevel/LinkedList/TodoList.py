# Định nghĩa class Node (một phần tử trong danh sách liên kết)
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self):
        return f"Node({self.data})"
    def __repr__(self):
        return f"Node(data={self.data}, next={repr(self.next)})"
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    def display(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
        else:
            print("Your to do list:")
            while current_node:
                print(f"- {current_node.data} (ID: {id(current_node)})")
                current_node = current_node.next
    def remove(self, key):
        # Trường hợp danh sách rỗng
        if self.head is None:
            print("Lists are empty")
        # Trường hợp nút cần xóa là nút đầu tiên
        if self.head.data == key:
            self.head = self.head.next
            print(f"{key} is removed")
            return
        # Duyệt qua danh sách để tìm nút cần xóa
        current_node = self.head
        while current_node:
            if current_node.next.data == key:
                print(f"Before {current_node.next}")
                current_node.next = current_node.next.next
                print(f"Founded {key}, After: {current_node.next}")
                return
            current_node = current_node.next
        print(f"Nut {key} is not existed in list")
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                print(f"Founded {key}")
                return
            current_node = current_node.next
        print(f"{key} not found")
    def update(self, oldValue, newTaskValue):
        current_node = self.head
        while current_node:
            if current_node.data == oldValue:
                current_node.data = newTaskValue
                return
            current_node = current_node.next
        print(f"{oldValue} not found")
    def count_nodes(self):
        current_node = self.head
        while current_node:
            count = count + 1
        print(f"Number of nodes is: ", count)
        return
def main():
    # Khởi tạo danh sách liên kết cho các nhiệm vụ
    todo_list = LinkedList()

    while True:
        print("\n=== Quản lý to-do list ===")
        print("1. Thêm nhiệm vụ")
        print("2. Hiển thị danh sách nhiệm vụ")
        print("3. Xóa nhiệm vụ")
        print("4. Tìm nhiệm vụ")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            task = input("Nhập nhiệm vụ mới: ")
            todo_list.append(task)
            print(f"Đã thêm nhiệm vụ '{task}' vào danh sách.")

        elif choice == "2":
            todo_list.display()

        elif choice == "3":
            task = input("Nhập nhiệm vụ muốn xóa: ")
            todo_list.remove(task)

        elif choice == "4":
            task = input("Nhập nhiệm vụ cần tìm: ")
            todo_list.search(task)

        elif choice == "5":
            task = input("Nhập nhiệm vụ cần cập nhật")
            newTaskValue = input(f"Nhập giá trị mới cho {task}")
            todo_list.update(task, newTaskValue)
        elif choice == "6":
            todo_list.count_nodes()
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
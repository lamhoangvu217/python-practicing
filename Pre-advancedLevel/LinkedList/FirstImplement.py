# basic first implement linkedlist in python
class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.__head = Node()
    def insert(self, value):
        new_node = Node(value) # tạo node mới
        new_node.next = self.__head.next 
        self.__head.next = new_node
    def display(self):
        current = self.__head.next
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
ll.insert(value=10)
ll.insert(value=20)
ll.insert(value=30)
ll.insert(value=40)
ll.insert(value=50)
ll.display()

# basic class implementation
class MyClass:
    def __init__(self, init_value, init_value2) -> None:
        self.value = init_value
        self.value2 = init_value2
    def print_hello(self):
        print(f'hello {self.value} {self.value2}')
obj1 = MyClass(init_value=900, init_value2=800)
print(obj1.print_hello())
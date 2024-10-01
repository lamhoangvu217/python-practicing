# Tính giai thừa
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
# Tính lũy thừa
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
# Tìm số fibonacci dự vào vị trí
def fibonacci(n):
    if n < 0:
        return "Số cần tính không hợp lệ"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False
# Menu để lựa chọn chức năng
def main_menu():
    print("Chọn chức năng:")
    print("1. Tính giai thừa")
    print("2. Tính lũy thừa")
    print("3. Tính số Fibonacci")
    print("4. Kiểm tra chuỗi Palindrome")
    print("5. Thoát")
def main():
    while True:
        main_menu()
        choice = input("Nhập lựa chọn của bạn (1-5): ")
        
        if choice == '1':
            n = int(input("Nhập số nguyên dương: "))
            result = factorial(n)
            print(f"Giai thừa của {n} là: {result}\n")
        
        elif choice == '2':
            x = int(input("Nhập cơ số (x): "))
            n = int(input("Nhập lũy thừa (n): "))
            result = power(x, n)
            print(f"{x}^{n} = {result}\n")
        
        elif choice == '3':
            n = int(input("Nhập vị trí trong dãy Fibonacci: "))
            result = fibonacci(n)
            print(f"Số Fibonacci thứ {n} là: {result}\n")
        
        elif choice == '4':
            s = input("Nhập chuỗi: ")
            if is_palindrome(s):
                print(f"'{s}' là chuỗi Palindrome.\n")
            else:
                print(f"'{s}' không phải là chuỗi Palindrome.\n")
        
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

# Chạy chương trình
if __name__ == "__main__":
    main()
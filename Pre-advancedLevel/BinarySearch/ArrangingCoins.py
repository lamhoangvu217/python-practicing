def arrangeCoins(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        total_coins = mid * (mid + 1) // 2  # Tính tổng số đồng xu cho mid hàng
        
        if total_coins == n:
            return mid  # Nếu số đồng xu đúng bằng n, trả về kết quả
        elif total_coins < n:
            left = mid + 1  # Có thể xây thêm hàng, tăng left
        else:
            right = mid - 1  # Tổng quá lớn, giảm right
    
    return right  # Giá trị lớn nhất của k sao cho tổng số đồng xu <= n

# Ví dụ
# n = 5
# print(arrangeCoins(n))  # Kết quả: 2
n = 8
print(arrangeCoins(n))  # Kết quả: 3
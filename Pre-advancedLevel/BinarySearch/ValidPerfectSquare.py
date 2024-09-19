# Leetcode: https://leetcode.com/problems/valid-perfect-square/description/

# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

# Example 1:
    # Input: num = 16
    # Output: true
    # Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
def isPerfectSquare(num):
        start = 1
        end = num
        while start <= end:
            mid = (start + end) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                start = mid + 1
            else:
                end = mid - 1
        return False

num = 5
print(isPerfectSquare(num))
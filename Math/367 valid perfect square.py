class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5==int(num**0.5)

#the time complexity is O(1) because we are only performing a constant number of operations regardless of the input size.
#the space complexity is O(1) because we are using a constant amount of space for the variables.

#alternate solution using binary search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
#the time complexity is O(log n) because we are performing a binary search on the range from 2 to num // 2.
#the space complexity is O(1) because we are using a constant amount of space for
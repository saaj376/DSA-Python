class Solution:
    def countEven(self, num: int) -> int:
        def digitSum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        count = 0
        for i in range(1, num + 1):
            if digitSum(i) % 2 == 0:
                count += 1
        return count

#the time complexity is O(n*log(n)) where n is the input number
#the space complexity is O(1) since we are using a constant amount of space
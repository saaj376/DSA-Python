class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5==int(num**0.5)

#the time complexity is O(1) because we are only performing a constant number of operations regardless of the input size.
#the space complexity is O(1) because we are using a constant amount of space for the variables.
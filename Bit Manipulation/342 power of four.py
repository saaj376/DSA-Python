class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

# This solution checks if n is a power of four using bit manipulation.
# we'll have to check if it's a power of two and if the number minus one is divisible by three. only then it is a power of four.
# The time complexity is O(1) because it only involves a few bitwise operations and arithmetic checks.
# The space complexity is O(1) because it uses a constant amount of space.
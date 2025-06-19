class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

#the time and space complexity of this solution is O(1) because it uses a constant amount of space and performs a constant number of operations regardless of the input size.
# 1162261467 is the largest power of 3 that fits in a 32-bit signed integer (3^19).
# This solution checks if n is a positive integer and if it divides 1162261467 evenly, which means n is a power of 3.
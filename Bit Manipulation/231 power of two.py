class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        if n%2==0:
            return self.isPowerOfTwo(n//2)
        return False
    
#this is the brute force solution, we can also use bit manipulation
#the time complexity is O(log n) because we are dividing n by 2 in each recursive call
#the space complexity is O(log n) because of the recursion stack



# Bit manipulation solution
# A number is a power of two if it has exactly one bit set in its binary representation
## This can be checked using the expression (n & (n - 1)) == 0
def isPowerOfTwoBitManipulation(self, n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# This solution has a time complexity of O(1) because it only involves a few bitwise operations
# The space complexity is O(1) because it uses a constant amount of space


#another solution using logarithm
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        ans=math.log2(n)
        return ans.is_integer()
    
# This solution has a time complexity of O(1) because it only involves a logarithm calculation
# The space complexity is O(1) because it uses a constant amount of space
from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num=int(''.join(str(x) for x in b))
        return pow(a,num,1337)

#using the pow function makes the time complexity O(log n) but since num can be a very large number (up to 2000 digits, e.g., 10^1999), the time complexity becomes O(d * log num). However, in practice, Python’s pow with a modulus is highly optimized, and the dominant cost is the string and integer conversion.
#so the final time complexity is O(d) where d is the number of digits in b.
#the space complexity is O(d) where d is the number of digits in b due to the string conversion.
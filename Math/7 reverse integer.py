class Solution:
    def reverse(self, x: int) -> int:
        ab=abs(x)
        reversed=int(str(ab)[::-1])
        if x<0:
            result=reversed*(-1)
        else:
            result=reversed
        if result <-2**31 or result >2**31 - 1:
            return 0
        return result

#the time complexity is O(logn) because we are converting the integer to a string and reversing it, which takes linear time relative to the number of digits in the integer.
#the space complexity is O(logn) due to the temporary strings created during the conversion process.
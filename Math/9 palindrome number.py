class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]
    
#the time complexity is O(n) where n is the number of digits in x
#the space complexity is O(n) where n is the number of digits in x
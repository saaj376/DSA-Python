class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_str=str(x)
        return x_str==x_str[::-1]
    
#the time complexity for the above code is O(n) because n is the number of digits that we're traversing.
#the space complexity O(n), due to storing both the string and its reversed version.
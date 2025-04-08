class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_str=str(x)
        return x_str==x_str[::-1]
    
#the time complexity for the above code is O(n) because n is the number of digits that we're traversing.
#the space complexity O(n), due to storing both the string and its reversed version.

class Solution:
    def ispalindrome(self,x:int)->bool:
        reversed=0
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0:
            return False
        while x>reversed:
            lastdigit=x%10
            reversed=reversed*10+lastdigit
            x=x//10
        return x==reversed or x==reversed//10
    #return x==reversed is for even digits
    #return x==reversed//10 for odd digits
#time complexity is O(logn) because we're reversing half of the digits
#space complexity is O(1) because only a few integer variables are used, no extra data structures or recursive calls are used hence constant space
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
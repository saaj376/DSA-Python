class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)
        while left<=right:
            sum=left**2+right**2
            if sum==c:
                return True
            elif sum<c:
                left+=1
            else:
                right-=1
        return False


#the time complexity is O(sqrt(c)) because we are iterating from 0 to sqrt(c) for the right pointer and from 0 to sqrt(c) for the left pointer, which gives us a total of O(sqrt(c)) iterations in the worst case.
#the space complexity is O(1) because we are using only a constant amount of space
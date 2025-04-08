class Solution:
    def reverseString(self, s: List[str]) -> None:
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1        

#the time complexity is O(n) because each element is visited only once and swapping is done in that time
#the space complexity is O(1) because it is done in place with no extra memory
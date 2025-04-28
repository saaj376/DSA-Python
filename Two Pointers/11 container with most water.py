class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maxarea=0
        while left<right:
            width=right-left
            minheight=min(height[left],height[right])
            area=width*minheight
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        
#the time complexity is O(n) where n is the length of the list.
#the space complexity is O(1) because we are using only a constant amount of space and no extra data structures is used.
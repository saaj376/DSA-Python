class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        water=0
        peak=0
        for i in range(n):
            if height[i]>height[peak]:
                peak=i
        maxleft=0
        for i in range(peak):
            if height[i]>maxleft:
                maxleft=height[i]
            else:
                water+=maxleft-height[i]
        maxright=0
        for i in range(n-1,peak,-1):
            if height[i]>maxright:
                maxright=height[i]
            else:
                water+=maxright-height[i]
        return water
    
#the time complexity is O(n) because we're traversing through the list in finding the peak, going from left to peak and from right to peak.
#the space complexity is O(1) because we're not using any extra space that grows with the input size.
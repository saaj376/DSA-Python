class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1=(ax2-ax1)*(ay2-ay1)
        rect2=(bx2-bx1)*(by2-by1)
        width=max(0,min(ax2,bx2)-max(ax1,bx1))
        height=max(0,min(ay2,by2)-max(ay1,by1))
        area=width*height
        return rect1+rect2-area
    
#the time and space complexity is O(1) because we're using constant arithmetic operations and no extra data structure is used
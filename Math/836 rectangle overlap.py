from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x=max(0,min(rec1[2],rec2[2])-max(rec1[0],rec2[0]))
        y=max(0,min(rec1[3],rec2[3])-max(rec1[1],rec2[1]))
        return x>0 and y>0
    
#both time and space complexity is O(1) because only basic arithmetic operations are used and no extra data structure is used.
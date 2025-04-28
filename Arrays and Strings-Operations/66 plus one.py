class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
    
#the time complexity is O(n) where n is the length of the array
#the space complexity is O(1) since we're modifying the array in place without using any additional data structures.
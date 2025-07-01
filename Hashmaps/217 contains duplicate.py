class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for char in nums:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in count:
            if count[char]>1:
                return True
        return False
    
#the total time complexity is O(n) since we're using two for loops O(n)+O(n)
#the space complexity is O(1) because we're using a dictionary of length of the list nums

#alternative solution

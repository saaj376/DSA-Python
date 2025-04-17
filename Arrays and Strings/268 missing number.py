class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        totalsum=(n*(n+1))//2
        arraysum=sum(nums)
        return totalsum-arraysum
    
#the time complexity is O(n) because when we're using sum() we're iterating through each variable of the list of 'n' elements.
#the space complexity is O(1) because we're not using any extra space and it does not use extra space.
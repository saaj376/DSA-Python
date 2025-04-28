class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        total=0
        for i in nums:
            total+=i
            maxsum=max(maxsum,total)
            if total<0:
                total=0
        return maxsum
    
#the time complexity is O(n) because we are iterating through the list once.
#the space complexity is O(1) because we are using only a few variables to store the sum and max sum.
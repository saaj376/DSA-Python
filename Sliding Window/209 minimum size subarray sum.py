class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minlength=float('inf')
        total=0
        n=len(nums)
        for right in range(n):
            total+=nums[right]
            while total>=target:
                w=right-left+1
                minlength=min(minlength,w)
                total-=nums[left]
                left+=1
        if minlength==float('inf'):
            return 0
        else:
            return minlength
        
#the time complexity is O(n) because we are using a sliding window approach, where we iterate through the array once with two pointers (left and right).
#the space complexity is O(1) because we are using a constant amount of extra space to store variables like left, minlength, total, and n.
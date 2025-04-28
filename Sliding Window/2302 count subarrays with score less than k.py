class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        n=len(nums)
        count=0
        total=0
        for right in range(n):
            total+=nums[right]
            while left<=right and total*(right-left+1)>=k:
                total-=nums[left]
                left+=1
            count+=(right-left+1)
        return count


#the time complexity of this solution is O(n) because we are using a sliding window approach, where both left and right pointers traverse the array once. The space complexity is O(1) because we are using only a constant amount of extra space for variables.
#the space complexity is O(1) because we are using only a constant amount of extra space for variables.
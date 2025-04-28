class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
        
#the time complexity is O(n) because we're traversing through the array once.
#the space complexity is O(1) because we're modifying the array in the loop itself. no extra data structures is used/created.
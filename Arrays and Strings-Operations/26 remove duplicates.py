class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

#the time complexity is O(n) because the loop runs once over the entire array
#no extra space is used, everything is done inside the list itself, only two pointers are used.
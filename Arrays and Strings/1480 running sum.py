class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
    
#time complexity is O(n) because it runs through all the iterations in the list
#space complexity is O(1)(auxilary space) because the operation is performed in place on the input list, no additional space other than the variable i is used.
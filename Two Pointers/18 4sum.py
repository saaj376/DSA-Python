class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lst=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        lst.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return list(lst)
    

#the time complexity is O(n³) because we're using two for loops and a while loop.
#the space complexity is O(k) where k is the number of quadruplets we found and sorting is in place, so no extra space is used.
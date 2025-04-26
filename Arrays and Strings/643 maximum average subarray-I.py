class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        currentsum=0
        for i in range(k):
            currentsum+=nums[i]
        maxavg=currentsum/k
        for i in range(k,n):
            currentsum+=nums[i]
            currentsum-=nums[i-k]
            avg=currentsum/k
            maxavg=max(avg,maxavg)

        return maxavg
    
#the time complexity is O(n) where n is the length of the input list and we're only iterating over it once so overall time complexity is linear.4
#the space complexity is O(1) because no extra space is allocated and only few integer variables are used.
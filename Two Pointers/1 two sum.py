class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numssorted=sorted(enumerate(nums),key=lambda x:x[1])
        left,right=0,len(numssorted)-1
        while left<right:
            total=numssorted[left][1]+numssorted[right][1]
            if total==target:
                return [numssorted[left][0],numssorted[right][0]]
            elif total<target:
                left+=1
            else:
                right-=1

#the time complexity is O(nlogn) because we're sorting the list and then traversing it once.'
#the space complexity is O(n) because we're storing the sorted list in a new variable.'

#alternate solution to this problem can be done using hashmaps
#the brute force solution is to use two loops and then check if the sum is equal to the target.
#the time complexity is O(n²) because we're using two loops and the space complexity is O(1) because we're not using any extra space.
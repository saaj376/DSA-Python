class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            total=numbers[right]+numbers[left]
            if total==target:
                return [left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1

#time complexity is O(n) because we're only traversing through the array once.
#space complexity is O(1) because we aren't creating any new data structures
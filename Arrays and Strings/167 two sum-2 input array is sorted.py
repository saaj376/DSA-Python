class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  
            elif total < target:
                left += 1  
            else:
                right -= 1  

#the time complexity is O(n)
#the space complexity is O(1)
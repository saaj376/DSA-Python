class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,j in enumerate(nums):
            a=target-j
            if a in hashmap:
                return [hashmap[a],i]
            hashmap[j]=i
        return []


#the time complexity is O(n) because we're using a for loop to traverse through the list
#the space complexity is O(n) because in worst case, we might store every element in the dictionary
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output=[]
        numset=set(nums)
        for i in range(1,len(nums)+1):
            if i not in numset:
                output.append(i)
        return output

#time complexity is o(n) because we're using set which makes it o(1) during lookup and traversing through each element of the list is o(n)
#space complexity is o(n) because numset stores all the elements and 'output' list for missing numbers-at most o(n) in worst cases      
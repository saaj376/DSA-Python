class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ddict = {}
        for num in nums1:
            if num in ddict:
                ddict[num] += 1
            else:
                ddict[num] = 1
        res = []
        for num in nums2:
            if num in ddict:
                res.append(num)
                del ddict[num]
        return res


#the time complexity is O(n + m) where n is the length of nums1 and m is the length of nums2
#the space complexity is O(n) where n is the length of nums1
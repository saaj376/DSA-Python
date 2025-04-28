class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
#the time complexity is O(n*m) where n is the length of haystack and m is the length of needle.
#the space complexity is O(1) because we are not using any extra space.
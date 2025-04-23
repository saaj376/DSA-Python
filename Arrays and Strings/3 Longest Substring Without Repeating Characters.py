class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        left=0
        length=0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[left])
                left+=1
            char.add(s[i])
            length=max(length,i-left+1)
        return length
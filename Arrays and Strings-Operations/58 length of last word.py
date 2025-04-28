class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        length=0
        for i in reversed(s):
            if i==" ":
                break
            length+=1
        return length

#the time complexity is O(n) where n is the length of the string s.
#the space complexity is O(1) because we are using only a constant amount of space.
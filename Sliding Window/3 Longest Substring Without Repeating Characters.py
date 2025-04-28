class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        sett=set()
        n=len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w=r-l+1
            longest=max(longest,w)
            sett.add(s[r])
        return longest
    
#the time complexity is O(n) because we're traversing the string of length n
#the space complexity is O(n) because we're storing the characters in a set which in worst case can be n characters.
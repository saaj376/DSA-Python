class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True

#the time complexity is O(n) because we're passing once through the string and ''.join(cleaned) also is O(n) and reversing string is also o(n)
#the space complexity is O(1) because we are not creating new strings or data structures
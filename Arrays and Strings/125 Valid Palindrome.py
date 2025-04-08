class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome=[]
        for i in s:
            if i.isalnum():
                palindrome.append(i.lower())
        palindromestring=''.join(palindrome)
        return palindromestring==palindromestring[::-1]

#the time complexity is O(n) because we're passing once through the string and ''.join(cleaned) also is O(n) and reversing string is also o(n)
#the space complexity is O(n) for the palindrome list and the reversed copy
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(s[::-1])

#the time complexity is O(n) because spliting of the lists take place, reversed copy of list is copied and joins words with space O(n)
#the space complexity is O(n) because in all the three steps, they all take up linear space so O(n)
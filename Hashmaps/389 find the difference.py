class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count={}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in t:
            if char not in count or count[char]==0:
                return char
            count[char]-=1

#We iterate through both strings exactly once: O(n) where n is the length of string s
#All operations on the hashmap (insert, get, check) are O(1) on average due to Python’s built-in dictionary implementation using hash tables
#thus the overall time complexity is O(n)

#We're storing the frequency of characters from string s in a dictionary.
#Since the input is guaranteed to be lowercase English letters, the maximum number of keys in the dictionary is 26.
#thus the total space complexity is O(1) in terms of the number of unique characters.
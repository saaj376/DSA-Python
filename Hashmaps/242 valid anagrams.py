#this is the brute force solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        
#the time complexity is O(nlogn) because sorted generally takes nlogn time because of the timsort algorithm of python

#optimal solution using hashmaps
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in t:
            if char not in count or count[char]==0:
                return False
            count[char]-=1
        return True


#the time complexity is O(n) totally because we're using two for loops
#the space complexity is O(1) because we're limited to only dealing with alphabets, if not restricted to alphabets, it would be O(n)
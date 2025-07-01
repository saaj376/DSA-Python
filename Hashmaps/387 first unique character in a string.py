#brute force approach
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in count:
            if count[char]==1:
                return s.index(char)
        return -1
                
#the time complexity is O(n²) because inside the for loop we're using a s.index() method and for worst case scenario, it is also O(n) which squares the worst time complexity
#the space complexity is O(1) since it's restricted to alphabets

#optimal solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for i,char in enumerate(s):
            if count[char]==1:
                return i
        return -1
    
#this brings the time complexity to O(n) and space complexity remains the same O(1) as long it is restricted to alphabets
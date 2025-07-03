class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count={}
        for char in stones:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        total=0
        for char in jewels:
            total+=count.get(char,0)
        return total
    

#the time complexity is O(n+m) where we're building a set of jewels O(m)
#and then we're iterating through stones O(n) and when we check in set it is O(1)
#the total time complexity is O(n+m)

#We're storing the set of jewel types → at most 26 characters if restricted to lowercase letters.
#So, worst-case space is O(m)
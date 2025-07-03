class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomnote_count={}
        magazine_count={}
        for char in ransomNote:
            if char in ransomnote_count:
                ransomnote_count[char]+=1
            else:
                ransomnote_count[char]=1
        for char in magazine:
            if char in magazine_count:
                magazine_count[char]+=1
            else:
                magazine_count[char]=1
        for char in ransomnote_count:
            if ransomnote_count[char]>magazine_count.get(char,0):
                return False
        return True  
    

# Time Complexity: O(n + m) where n is the length of ransomNote and m is the length of magazine.
# Space Complexity: O(1) because we're using only alphabet characters (constant space for the hashmap).
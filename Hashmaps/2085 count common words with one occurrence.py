class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1={}
        for char in words1:
            if char in count1:
                count1[char]+=1
            else:
                count1[char]=1
    
        count2={}
        for char in words2:
            if char in count2:
                count2[char]+=1
            else:
                count2[char]=1
        
        result=0
        for i in count1:
            if count1[i]==1 and count2.get(i,0)==1:
                result+=1
        return result
    
# Time Complexity: O(n + m), where n is the length of words1 and m is the length of words2 and O(n) is the worst case for the dictionary operationns because average dictionary operations are O(1).
# Space Complexity: O(n + m), where n is the length of words1 and m is the length of words2, as we are storing the counts of each word in two separate dictionaries.
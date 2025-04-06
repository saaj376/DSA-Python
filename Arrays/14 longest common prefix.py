class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
#time complexity is O(S*M) where S is the sum of all characters across all strings in the input list and M is the length of the initial prefix
#space complexity is O(1) where only a single variable is getting modified and no additional memory is used.
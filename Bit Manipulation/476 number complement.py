class Solution:
    def findComplement(self, num):
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
    
#I didn't understand the logic behind this solution, but it works. Have to look into it later.
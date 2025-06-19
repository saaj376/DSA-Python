class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        return 1+(num-1)%9
    
#this formula was new to me
#the time complexity is O(1) because it only involves a few arithmetic operations
#the space complexity is O(1) because it uses a constant amount of space

#this formula is the digital root formula, which is a well-known mathematical property of numbers
#it states that the digital root of a number can be found using the formula 1 + (num - 1) % 9
#this works because the digital root is the same as the remainder when the number is divided by 9, except for the case when the number is 0, where the digital root is also 0
#brute force solution
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            if i%2!=0:
                c+=1
        return c

#the time complexity is O(high-low) and not suitable for large intervals
#the space complexity is O(1) since we are using a constant amount of space

#optimized solution
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1
    
#time and space complexity is O(1) since we are using a constant amount of space and time
#this solution works because we are counting the number of odd numbers in the interval [low, high]
#we first check if low is even, if it is we increment it by 1 to make it odd
#we then check if high is even, if it is we decrement it by 1 to make it odd
#finally we calculate the number of odd numbers in the interval by subtracting low from high and dividing by 2
#we add 1 to the result to include the last odd number in the interval if it exists
#this solution works in O(1) time and space complexity
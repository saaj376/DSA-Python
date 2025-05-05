class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
#the time complexity is O(n) and the space complexity is O(1)
#the time complexity is O(n) because we are iterating through the list of prices once 
#the space complexity is O(1) because we are using only a constant amount of space to store the min_price and max_profit variables
#the algorithm is a sliding window algorithm because we are keeping track of the minimum price seen so far and the maximum profit that can be made at each step
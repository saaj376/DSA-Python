class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        for i in str(n):
            product*=int(i)
            sum+=int(i)
        return product-sum

# the time complexity is O(logn) because we are iterating through the digits of n and not directly through n.
# the space complexity is O(logn) because we are storing the digits of n in a string.
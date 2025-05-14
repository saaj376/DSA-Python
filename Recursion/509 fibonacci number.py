class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)
        
# Time complexity: O(2^n) Exponential time due to repeated calculations and branching of two recursive calls per invocation.
# Space complexity: O(n) for the recursion stack, as the maximum depth of the recursion is n.
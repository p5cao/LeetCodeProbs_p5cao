class Solution:
    def climbStairs(self, n: int) -> int:
        # easiest solution: bottom up DP => Fibonacci 
        sum_n_1, sum_n_2 = 1, 1
        
        for i in range(n-1):
            temp = sum_n_1
            sum_n_1 = sum_n_1 + sum_n_2
            sum_n_2 = temp
        return sum_n_1

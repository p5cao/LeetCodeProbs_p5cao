class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hashMap = {}
        maxP = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # if right ptr smaller than left ptr, make left ptr equal to right ptr
                l = r
            r+=1
        return maxP   
import numpy as np
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [np.inf] * (amount + 1)
        
        DP[0] = 0
        for a in range(1, amount +1):
            for c in coins:
                if a - c >= 0:
                    DP[a] = min(DP[a], 1 + DP[a-c]) # update DP values
        return DP[amount] if DP[amount]!= np.inf else -1 
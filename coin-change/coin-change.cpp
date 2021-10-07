class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // double inf = std::numeric_limits<double>::infinity();
        // vector<double> DP(amount+1, inf);
        int Max = amount + 1;
        vector<int> DP(amount + 1, Max);
        DP[0] = 0;
        for (int a = 1; a< amount+1; a++){
            for (int i = 0; i< coins.size(); i++){
                if (a >= coins[i]){
                    DP[a] = min(DP[a], 1 + DP[a-coins[i]]);
                }
            }
        }
        
        if (DP[amount] != amount + 1){
            return DP[amount];
        }else{
            return -1;
        }
    }
};
                 
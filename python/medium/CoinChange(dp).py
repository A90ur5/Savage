from collections import defaultdict

class Solution:
    def initdict(self):
        return 10002

    def dfs(self, amount, coins, dp):
        if dp[amount] != 10002:
            return dp[amount]

        if amount == 0:
            dp[amount] = 0
            return 0

        minCoin = 10001
        for c in coins:
            if c <= amount:
                minCoin = min(minCoin, self.dfs(amount-c, coins, dp) + 1)

        dp[amount] = minCoin
        return minCoin
                
        

    #def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount) -> int:
        dp = defaultdict(self.initdict)
        coins.sort(reverse=True)
        if amount == 0:
            return 0
        minCoin = self.dfs(amount, coins, dp)
        if minCoin > 10000:
            return -1
        else:
            return minCoin

if __name__ == '__main__':
    ans = Solution()
    testData = [2]
    print(ans.coinChange(testData, 3))
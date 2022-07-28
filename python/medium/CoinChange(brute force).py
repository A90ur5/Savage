class Solution:
    def dfs(self, amount, coins):
        if amount == 0:
            return 0
        minCoin = 10001
        for c in coins:
            if c <= amount:
                minCoin = min(minCoin, self.dfs(amount-c, coins) + 1)

        return minCoin
                
        

    #def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount) -> int:
        if amount == 0:
            return 0
        minCoin = self.dfs(amount, coins)
        if minCoin == 10001:
            return -1
        else:
            return minCoin

if __name__ == '__main__':
    ans = Solution()
    testData = [1, 3, 5]
    print(ans.coinChange(testData, 40))
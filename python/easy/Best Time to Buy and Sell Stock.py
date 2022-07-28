class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max = prices[0]
        min = prices[0]
        maxProfit = 0
        for price in prices:
            if price > max:
                max = price
            elif price < min:
                if max - min > maxProfit:
                    maxProfit = max - min
                min = price
                max = price
        if max - min > maxProfit:
            maxProfit = max - min
        return profit
            
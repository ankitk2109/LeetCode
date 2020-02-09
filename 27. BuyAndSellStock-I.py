#Problem available at: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (prices):
            p = prices
            n = len(p)
            max_profit = 0
            buy = prices[0]
            for i in range(1, n):
                if p[i] - buy < 0:
                    buy = p[i]
                else:
                    if max_profit < p[i] - buy:
                        max_profit = p[i] - buy
            return max_profit
        else:
            return 0
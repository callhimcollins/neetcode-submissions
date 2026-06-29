class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        l, r = 0, n - 1

        for r in range(n):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            if prices[r] < prices[l]:
                l = r
        
        return maxProfit
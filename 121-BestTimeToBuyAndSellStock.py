class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            else:
                l = r

        return maxProfit

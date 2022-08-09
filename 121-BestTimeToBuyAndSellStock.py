def maxProfit(prices):
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r += 1

    return maxProfit

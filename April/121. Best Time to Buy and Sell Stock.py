class Solution:
    def maxProfit(self, prices) -> int:
        minprice = max(prices)+1
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

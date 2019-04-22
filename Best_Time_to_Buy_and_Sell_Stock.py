class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        lowestBuyCost = prices[0]
        highestProfit = 0
        latestBuyDay = 0
        for sellDay in range(1, len(prices)):
            highestProfit = max(highestProfit, prices[sellDay]-lowestBuyCost)
            latestBuyDay += 1
            lowestBuyCost = min(lowestBuyCost, prices[latestBuyDay])
        return highestProfit
            

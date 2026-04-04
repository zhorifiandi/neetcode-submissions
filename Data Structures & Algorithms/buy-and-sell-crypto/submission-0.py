class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for buy_time in range(n):
            for sell_time in range(buy_time + 1, n):
                if prices[sell_time] < prices[buy_time]:
                    break
                
                profit = max(profit, prices[sell_time] - prices[buy_time])
        
        return profit

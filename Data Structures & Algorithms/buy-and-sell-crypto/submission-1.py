class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        
        buy_time, sell_time = 0, 1
        while sell_time < n:
            if prices[sell_time] < prices[buy_time]:
                buy_time = sell_time
                
            profit = max(profit, prices[sell_time] - prices[buy_time])
            sell_time += 1
        
        return profit

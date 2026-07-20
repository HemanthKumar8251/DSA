class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        # Time Limit Exceeded O(n**2) Solution
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         max_profit = max(max_profit,prices[j]-prices[i])
        # return max_profit

        # Using Kadane's Algorithm
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy = prices[i]
            profit = max(profit, prices[i]-buy)
        return profit
            
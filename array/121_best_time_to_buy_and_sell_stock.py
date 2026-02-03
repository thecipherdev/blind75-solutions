from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                current_profit = prices[sell] - prices[buy]
                profit = max(profit, current_profit)
            else:
                buy = sell
            sell += 1

        return profit


sol = Solution()


print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))

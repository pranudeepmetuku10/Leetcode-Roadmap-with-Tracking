"""
Problem: Best Time to Buy and Sell Stock
LeetCode #: 121
Difficulty: Easy
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Pattern: Sliding Window / Array
Companies: Amazon, Microsoft, Google, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check every buy/sell pair
- Time: O(n²)  |  Space: O(1)

Optimal:
- Track minimum price seen so far
- For each price, calculate profit if sold at this price
- Key Insight: Only care about minimum before current, not pairs
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We want maximum profit from one buy and sell. The brute force checks
all pairs. But we only need to track the minimum price seen so far,
and for each price calculate profit if we sell now. This is O(n)."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Check all buy/sell pairs.
        """
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit


# ─── Optimal ───
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Track minimum price, calculate profit at each step.
        """
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        
        return max_profit


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test 2: Decreasing prices
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test 3: Profit at end
    assert sol.maxProfit([2, 4, 1, 7, 5, 11]) == 10
    
    # Test 4: Two prices
    assert sol.maxProfit([2, 4]) == 2
    
    print("All tests passed!")

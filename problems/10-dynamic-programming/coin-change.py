"""
Problem: Coin Change
LeetCode #: 322
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Recursion: try each coin and recurse on remaining amount
- Time: O(amount^coins)  |  Space: O(amount)

Optimal:
- DP: dp[i] = min coins to make amount i
- For each amount, try each coin and take minimum
- dp[i] = 1 + min(dp[i - coin]) for all valid coins
- Key Insight: Build up from 0 to target amount
- Time: O(amount * coins)  |  Space: O(amount)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To find the minimum coins for an amount, we use DP. For each amount from
1 to target, we try each coin. If we use that coin, we add 1 to the result
of (amount - coin). We track the minimum across all coin choices. Start
with amount 0 = 0 coins."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Recursion with memoization.
        """
        memo = {}
        
        def helper(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            if remaining in memo:
                return memo[remaining]
            
            min_coins = float('inf')
            for coin in coins:
                result = helper(remaining - coin)
                if result >= 0:
                    min_coins = min(min_coins, 1 + result)
            
            memo[remaining] = min_coins if min_coins != float('inf') else -1
            return memo[remaining]
        
        return helper(amount)


# ─── Optimal ───
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DP bottom-up - O(amount * coins) time.
        """
        # dp[i] = min coins to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins needed for amount 0
        
        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    # Use this coin and recurse on remaining
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    assert sol.coinChange([1, 2, 5], 5) == 1
    
    # Test 2: Multiple coins needed
    assert sol.coinChange([2], 3) == -1
    
    # Test 3: Example from problem
    assert sol.coinChange([10], 10) == 1
    
    # Test 4: Complex case
    assert sol.coinChange([1, 3, 4], 6) == 2
    
    print("All tests passed!")

"""
Problem: Longest Increasing Subsequence
LeetCode #: 300
Difficulty: Medium
URL: https://leetcode.com/problems/longest-increasing-subsequence/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check all subsequences, find longest increasing one
- Time: O(2^n)  |  Space: O(n)

Optimal:
- DP: dp[i] = length of LIS ending at index i
- For each i, check all j < i where nums[j] < nums[i]
- dp[i] = 1 + max(dp[j])
- Key Insight: Build on previously computed LIS values
- Time: O(n²)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"For each position, we find the longest increasing subsequence ending at that
position. We check all previous positions with smaller values. If we append
the current number to those sequences, we get a longer increasing subsequence.
We track the maximum across all positions."

"""
from typing import List
import bisect


# ─── Brute Force ───
class BruteForceSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Recursion with memoization.
        """
        memo = {}
        
        def helper(index, prev_val):
            if index == len(nums):
                return 0
            if (index, prev_val) in memo:
                return memo[(index, prev_val)]
            
            # Skip current number
            skip = helper(index + 1, prev_val)
            
            # Include current number if valid
            include = 0
            if nums[index] > prev_val:
                include = 1 + helper(index + 1, nums[index])
            
            result = max(skip, include)
            memo[(index, prev_val)] = result
            return result
        
        return helper(0, float('-inf'))


# ─── Optimal ───
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DP - O(n²) time, O(n) space.
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # dp[i] = length of LIS ending at index i
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                # If nums[j] < nums[i], we can append i to LIS ending at j
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    # Test 2: Decreasing sequence
    assert sol.lengthOfLIS([0]) == 1
    
    # Test 3: All increasing
    assert sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 8]) == 6
    
    # Test 4: Single element
    assert sol.lengthOfLIS([0]) == 1
    
    print("All tests passed!")

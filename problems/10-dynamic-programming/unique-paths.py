"""
Problem: Unique Paths
LeetCode #: 62
Difficulty: Medium
URL: https://leetcode.com/problems/unique-paths/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Recursion: from each cell, explore right or down
- Time: O(2^(m+n))  |  Space: O(m+n)

Optimal:
- DP: dp[i][j] = ways to reach (i,j)
- Can only come from top or left
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Key Insight: Builds on smaller path counts
- Time: O(m*n)  |  Space: O(m*n) or O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To reach cell (i,j), you either came from above (i-1,j) or from the left
(i,j-1). So the number of ways to reach (i,j) is the sum of ways to reach
those two cells. Start with 1 way to reach any cell in the first row or
column. Compute all cells using this recurrence."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Recursion with memoization.
        """
        memo = {}
        
        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = helper(i + 1, j) + helper(i, j + 1)
            memo[(i, j)] = result
            return result
        
        return helper(0, 0)


# ─── Optimal ───
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        DP bottom-up - O(m*n) time, O(n) space.
        """
        # Only need previous row
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                # Paths = paths from above + paths from left
                dp[j] += dp[j - 1]
        
        return dp[n - 1]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 3x7 grid
    assert sol.uniquePaths(3, 7) == 28
    
    # Test 2: 3x3 grid
    assert sol.uniquePaths(3, 3) == 6
    
    # Test 3: 1x1 grid
    assert sol.uniquePaths(1, 1) == 1
    
    # Test 4: Single row
    assert sol.uniquePaths(1, 10) == 1
    
    print("All tests passed!")

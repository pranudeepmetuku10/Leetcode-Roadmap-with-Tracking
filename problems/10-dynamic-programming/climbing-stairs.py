"""
Problem: Climbing Stairs
LeetCode #: 70
Difficulty: Easy
URL: https://leetcode.com/problems/climbing-stairs/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Recursion: to reach n, reach n-1 then +1 step or n-2 then +2 steps
- Time: O(2^n)  |  Space: O(n)

Optimal:
- DP: dp[i] = ways to reach step i = dp[i-1] + dp[i-2]
- Similar to Fibonacci sequence
- Key Insight: Each step reuses previous results
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To reach step n, we either came from step n-1 (with 1 step) or step n-2
(with 2 steps). So ways to reach n equals ways to reach n-1 plus ways to
reach n-2. This is the Fibonacci pattern. We build up from base cases:
1 way to reach step 1, 2 ways to reach step 2."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def climbStairs(self, n: int) -> int:
        """
        Recursion without memoization - O(2^n) time.
        """
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# ─── Optimal ───
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        DP with O(1) space - iterate bottom-up.
        """
        if n <= 2:
            return n
        
        # Only need last two values
        prev2, prev1 = 1, 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n=2
    assert sol.climbStairs(2) == 2
    
    # Test 2: n=3
    assert sol.climbStairs(3) == 3
    
    # Test 3: n=1
    assert sol.climbStairs(1) == 1
    
    # Test 4: n=5
    assert sol.climbStairs(5) == 8
    
    print("All tests passed!")

"""
Problem: Decode Ways
LeetCode #: 91
Difficulty: Medium
URL: https://leetcode.com/problems/decode-ways/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Backtracking: try single and double digit decodings
- Time: O(2^n)  |  Space: O(n)

Optimal:
- DP: dp[i] = ways to decode s[0:i]
- If digit is 0, can't decode alone
- If digits form valid 2-digit code, add dp[i-2]
- Otherwise add dp[i-1]
- Key Insight: Track valid decodings up to each position
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We count the number of ways to decode a string where digits can be single
(1-9) or double digits (10-26). At each position, if the current digit is
non-zero, we can decode it alone. If the last two digits form a valid code
(10-26), we can decode them together. Total ways is sum of both options."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def numDecodings(self, s: str) -> int:
        """
        Backtracking approach.
        """
        memo = {}
        
        def helper(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]
            
            result = helper(index + 1)
            
            # Try 2-digit decode
            if index + 1 < len(s):
                two_digit = int(s[index:index + 2])
                if 10 <= two_digit <= 26:
                    result += helper(index + 2)
            
            memo[index] = result
            return result
        
        return helper(0) if s and s[0] != '0' else 0


# ─── Optimal ───
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        DP - O(n) time, O(1) space.
        """
        if not s or s[0] == '0':
            return 0
        
        # prev2 = ways to decode up to i-2
        # prev1 = ways to decode up to i-1
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            
            # Single digit decode
            if s[i] != '0':
                current = prev1
            
            # Two digit decode
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += prev2
            
            # Not valid to decode either way
            if current == 0:
                return 0
            
            prev2 = prev1
            prev1 = current
        
        return prev1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple ways
    assert sol.numDecodings("12") == 2
    
    # Test 2: Single way
    assert sol.numDecodings("226") == 3
    
    # Test 3: No valid ways
    assert sol.numDecodings("0") == 0
    
    # Test 4: Leading zero invalid
    assert sol.numDecodings("06") == 0
    
    print("All tests passed!")

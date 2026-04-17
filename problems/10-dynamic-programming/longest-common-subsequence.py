"""
Problem: Longest Common Subsequence
LeetCode #: 1143
Difficulty: Medium
URL: https://leetcode.com/problems/longest-common-subsequence/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Generate all subsequences of both strings, find common ones
- Time: O(2^m * 2^n)  |  Space: O(m+n)

Optimal:
- DP: dp[i][j] = LCS length for text1[0:i] and text2[0:j]
- If chars match: dp[i][j] = dp[i-1][j-1] + 1
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Key Insight: 2D DP builds on overlapping subproblems
- Time: O(m*n)  |  Space: O(m*n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"For longest common subsequence, we use 2D DP. If characters match, we extend
the LCS from previously matched characters. If they don't match, we take the
better result of either removing the character from text1 or text2. Build a
table computing all subproblems."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Recursion with memoization.
        """
        memo = {}
        
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                result = 1 + helper(i + 1, j + 1)
            else:
                result = max(helper(i + 1, j), helper(i, j + 1))
            
            memo[(i, j)] = result
            return result
        
        return helper(0, 0)


# ─── Optimal ───
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DP 2D table - O(m*n) time and space.
        """
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length for text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters don't match, take better option
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    assert sol.longestCommonSubsequence("abcde", "ace") == 3
    
    # Test 2: No common
    assert sol.longestCommonSubsequence("abc", "def") == 0
    
    # Test 3: Identical strings
    assert sol.longestCommonSubsequence("abc", "abc") == 3
    
    # Test 4: One is subset
    assert sol.longestCommonSubsequence("ox", "carboxils") == 2
    
    print("All tests passed!")

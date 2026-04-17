"""
Problem: Word Break
LeetCode #: 139
Difficulty: Medium
URL: https://leetcode.com/problems/word-break/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Backtracking: try removing each word from start
- Time: O(2^n)  |  Space: O(n)

Optimal:
- DP: dp[i] = can form s[0:i] using words in dict
- For each position, check if any word ending at i matches
- dp[i] = any dp[j] where s[j:i] is in dict
- Key Insight: Build from smaller subproblems
- Time: O(n²)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We use DP to check if we can break the string using dictionary words. For
each position, we check if there's a valid word ending at that position.
If the substring from some valid position to current is in the dictionary,
then current position is also valid. Build up from position 0."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Backtracking approach.
        """
        word_set = set(wordDict)
        
        def helper(index):
            if index == len(s):
                return True
            
            for word in word_set:
                if s[index:].startswith(word):
                    if helper(index + len(word)):
                        return True
            
            return False
        
        return helper(0)


# ─── Optimal ───
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        DP - O(n²) time, O(n) space.
        """
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] = can form s[0:i]
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be formed
        
        for i in range(1, n + 1):
            for j in range(i):
                # If we can form s[0:j] and s[j:i] is a word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Can break
    assert sol.wordBreak("leetcode", ["leet", "code"]) == True
    
    # Test 2: Can break with different split
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) == True
    
    # Test 3: Cannot break
    assert sol.wordBreak("catsandog", ["cat", "cats", "and", "sand", "dog"]) == False
    
    # Test 4: Single word
    assert sol.wordBreak("a", ["a"]) == True
    
    print("All tests passed!")

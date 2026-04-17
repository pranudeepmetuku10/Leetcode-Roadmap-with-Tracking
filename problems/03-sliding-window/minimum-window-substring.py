"""
Problem: Minimum Window Substring
LeetCode #: 76
Difficulty: Hard
URL: https://leetcode.com/problems/minimum-window-substring/

Pattern: Sliding Window
Companies: Amazon, Google, Meta, Microsoft, Bloomberg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Generate all substrings and check if valid
- Time: O(n³)  |  Space: O(n)

Optimal:
- Sliding window with two hashmaps (needed and found)
- Expand right until all characters satisfied
- Shrink left while valid, track minimum window
- Key Insight: Track what letters we need and what we have
- Time: O(n)  |  Space: O(1) (at most 52 chars - uppercase + lowercase)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need the shortest substring containing all required characters.
Using sliding window: track what we need (from target) and what we have
(from current window). Expand right to get more characters, then shrink
left while the window is still valid. Track the minimum window found."

"""
from collections import defaultdict


# ─── Brute Force ───
class BruteForceSolution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Check all substrings.
        """
        from collections import Counter
        
        if not t or not s:
            return ""
        
        target_count = Counter(t)
        result = ""
        min_length = float('inf')
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                sub_count = Counter(substring)
                
                # Check if substring contains all required chars
                if all(sub_count[char] >= target_count[char] for char in target_count):
                    if len(substring) < min_length:
                        min_length = len(substring)
                        result = substring
        
        return result


# ─── Optimal ───
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window with required/have counters.
        """
        if not t or not s:
            return ""
        
        # Count required characters
        required = {}
        for char in t:
            required[char] = required.get(char, 0) + 1
        
        # Window with these characters found
        window = {}
        
        # Number of unique characters with desired frequency
        formed = 0
        required_len = len(required)
        
        # Result: (window length, left, right)
        result = float('inf'), None, None
        
        left = 0
        for right in range(len(s)):
            # Add character from the right
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Check if frequency of current character matches required
            if char in required and window[char] == required[char]:
                formed += 1
            
            # Shrink from left while valid
            while left <= right and formed == required_len:
                # Update result if this window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove character from left
                char = s[left]
                window[char] -= 1
                if char in required and window[char] < required[char]:
                    formed -= 1
                
                left += 1
        
        # Return the smallest window or empty string
        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test 2: All same character
    assert sol.minWindow("a", "a") == "a"
    
    # Test 3: No valid window
    assert sol.minWindow("a", "aa") == ""
    
    # Test 4: Multiple matches
    result = sol.minWindow("aa", "aa")
    assert result == "aa"
    
    print("All tests passed!")

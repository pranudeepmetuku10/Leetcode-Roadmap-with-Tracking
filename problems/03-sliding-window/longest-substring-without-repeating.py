"""
Problem: Longest Substring Without Repeating Characters
LeetCode #: 3
Difficulty: Medium
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern: Sliding Window
Companies: Amazon, Google, Meta, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check all substrings for repeating characters
- Time: O(n³)  |  Space: O(n)

Optimal:
- Use sliding window with character position map
- Expand right pointer, shrink left when duplicate found
- Track maximum window size
- Key Insight: Map stores last seen position of each character
- Time: O(n)  |  Space: O(min(n, 26))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We want the longest substring without any repeating characters.
Using a sliding window: expand the right pointer, track character
positions in a map. When we see a duplicate, shrink from the left
until the duplicate is removed. Track maximum window size. This is O(n)."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Check all substrings.
        """
        max_length = 0
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if len(substring) == len(set(substring)):  # No duplicates
                    max_length = max(max_length, len(substring))
        
        return max_length


# ─── Optimal ───
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with character position map.
        """
        char_index = {}  # char -> last seen index
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If character was seen and is in current window, shrink
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            # Update character's last position
            char_index[char] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: With repeating characters
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    
    # Test 2: All unique
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    
    # Test 3: No repeating at end
    assert sol.lengthOfLongestSubstring("pwwkew") == 3  # "wke"
    
    # Test 4: Empty string
    assert sol.lengthOfLongestSubstring("") == 0
    
    print("All tests passed!")

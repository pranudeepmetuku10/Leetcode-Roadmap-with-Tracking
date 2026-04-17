"""
Problem: Longest Repeating Character Replacement
LeetCode #: 424
Difficulty: Medium
URL: https://leetcode.com/problems/longest-repeating-character-replacement/

Pattern: Sliding Window
Companies: Google, Meta, Amazon, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Try all substrings and check if replaceable
- Time: O(n²)  |  Space: O(26)

Optimal:
- Sliding window tracking character frequencies
- Window is valid if: length - max_freq <= k replacements allowed
- Key Insight: Track max frequency, not individual counts after removal
- Time: O(n)  |  Space: O(26)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We want the longest substring where we can make all characters the same
with k replacements. Using sliding window: expand right, track character
frequencies. The window is valid if we can replace all non-majority chars
with k operations. Shrink left when invalid. This is O(n)."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Check all substrings.
        """
        max_length = 0
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                # Find most frequent character
                from collections import Counter
                counts = Counter(substring)
                max_freq = max(counts.values()) if counts else 0
                replacements = len(substring) - max_freq
                
                if replacements <= k:
                    max_length = max(max_length, len(substring))
        
        return max_length


# ─── Optimal ───
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window with frequency tracking.
        """
        char_count = {}
        max_length = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Add character at right pointer
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])
            
            # Check if window is valid
            # Window length - most frequent char = replacements needed
            window_length = right - left + 1
            replacements_needed = window_length - max_freq
            
            # Shrink window if too many replacements needed
            if replacements_needed > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Can form with 2 replacements
    assert sol.characterReplacement("ABAB", 2) == 4
    
    # Test 2: Partial match
    assert sol.characterReplacement("AABABBA", 1) == 4
    
    # Test 3: Single character
    assert sol.characterReplacement("AAAA", 0) == 4
    
    # Test 4: All different
    assert sol.characterReplacement("ABCDE", 1) == 2
    
    print("All tests passed!")

"""
Problem: Valid Anagram
LeetCode #: 242
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/

Pattern: HashMap
Companies: Google, Amazon, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Sort both strings and compare them
- Time: O(n log n)  |  Space: O(1) (not counting sort space)

Optimal:
- Count character frequencies in both strings and compare
- Key Insight: Anagrams have identical character counts
- Time: O(n)  |  Space: O(1) (at most 26 characters)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"An anagram means both strings use the same letters with the same frequencies.
We could sort and compare, but a better approach is to count character frequencies
using a HashMap, then compare the counts. This is O(n) with constant space."

"""
from typing import Counter


# ─── Brute Force ───
class BruteForceSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Sort both strings and compare - O(n log n) time.
        """
        return sorted(s) == sorted(t)


# ─── Optimal ───
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Compare character frequency counts.
        """
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract character counts from t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return True


# ─── Optimal (using Counter) ───
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Using Counter from collections module.
        """
        from collections import Counter
        return Counter(s) == Counter(t)


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid anagram
    assert sol.isAnagram("anagram", "nagaram") == True
    
    # Test 2: Not an anagram
    assert sol.isAnagram("rat", "car") == False
    
    # Test 3: Different lengths
    assert sol.isAnagram("a", "ab") == False
    
    # Test 4: Single character
    assert sol.isAnagram("a", "a") == True
    
    print("All tests passed!")

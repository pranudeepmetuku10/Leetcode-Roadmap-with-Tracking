"""
Problem: Valid Palindrome
LeetCode #: 125
Difficulty: Easy
URL: https://leetcode.com/problems/valid-palindrome/

Pattern: Two Pointers
Companies: Amazon, Microsoft, Google, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Clean string, then check if it equals its reverse
- Time: O(n)  |  Space: O(n)

Optimal:
- Use two pointers from both ends moving inward
- Skip non-alphanumeric characters
- Compare characters (case-insensitive)
- Key Insight: Two pointers eliminate need for extra space
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to check if a string is a valid palindrome, ignoring spaces
and special characters. We could clean the string then check, but a
better approach is two pointers: start at both ends and move inward,
skipping non-alphanumeric characters. This is O(n) with O(1) space."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def isPalindrome(self, s: str) -> bool:
        """
        Clean string and check if it equals reverse.
        """
        # Keep only alphanumeric, convert to lowercase
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]


# ─── Optimal ───
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointers with O(1) space.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric on left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric on right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid palindrome with spaces and punctuation
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    
    # Test 2: Invalid palindrome
    assert sol.isPalindrome("race a car") == False
    
    # Test 3: Only spaces
    assert sol.isPalindrome(" ") == True
    
    # Test 4: Single character
    assert sol.isPalindrome("a") == True
    
    print("All tests passed!")

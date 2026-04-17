"""
Problem: Container With Most Water
LeetCode #: 11
Difficulty: Medium
URL: https://leetcode.com/problems/container-with-most-water/

Pattern: Two Pointers
Companies: Google, Amazon, Meta, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check all pairs of heights to find maximum area
- Time: O(n²)  |  Space: O(1)

Optimal:
- Use two pointers from both ends
- Area = width × min(left_height, right_height)
- Move the pointer with smaller height inward (only way to possibly increase area)
- Track maximum area seen
- Key Insight: Move smaller height pointer because moving larger can only decrease
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to find two heights that create the maximum area. The brute force
checks all pairs in O(n²). But using two pointers: start at both ends.
The area is width times the minimum height. Always move the pointer with the
smaller height inward, because that's the only way to potentially increase area."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def maxArea(self, height: List[int]) -> int:
        """
        Check all pairs of heights.
        """
        max_area = 0
        
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                h = min(height[i], height[j])
                area = width * h
                max_area = max(max_area, area)
        
        return max_area


# ─── Optimal ───
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Use two pointers from both ends.
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area with current pointers
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)
            
            # Move the pointer with the smaller height
            # (only way to possibly get larger area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test 2: Simple case
    assert sol.maxArea([1, 1]) == 1
    
    # Test 3: Increasing then decreasing
    assert sol.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
    
    # Test 4: All same height
    assert sol.maxArea([1, 1, 1, 1]) == 3
    
    print("All tests passed!")

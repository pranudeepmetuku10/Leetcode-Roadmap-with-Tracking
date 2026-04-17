"""
Problem: Binary Search
LeetCode #: 704
Difficulty: Easy
URL: https://leetcode.com/problems/binary-search/

Pattern: Binary Search
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Linear search through the array
- Time: O(n)  |  Space: O(1)

Optimal:
- Use binary search to eliminate half the search space each iteration
- Start with left=0, right=len(arr)-1
- Compare mid element with target and move pointers
- Key Insight: Only works on SORTED arrays
- Time: O(log n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to find a target in a sorted array. Linear search would be O(n),
but since it's sorted, we can use binary search. We maintain left and right
pointers, check the middle element, and eliminate half the search space each
time. This gives us O(log n) time complexity with O(1) space."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Linear search - O(n) time.
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# ─── Optimal ───
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search - O(log n) time.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Target in the middle
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    
    # Test 2: Target not found
    assert sol.search([-1, 0, 3, 5, 9, 12], 13) == -1
    
    # Test 3: Target at start
    assert sol.search([5], 5) == 0
    
    # Test 4: Single element not found
    assert sol.search([5], 3) == -1
    
    print("All tests passed!")

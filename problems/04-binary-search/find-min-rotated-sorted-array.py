"""
Problem: Find Minimum in Rotated Sorted Array
LeetCode #: 153
Difficulty: Medium
URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Pattern: Binary Search
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Linear scan through array to find minimum
- Time: O(n)  |  Space: O(1)

Optimal:
- Use binary search, but handle the rotation
- Identify which half is sorted, then search the unsorted half
- The minimum is at the rotation point
- Key Insight: In a rotated sorted array, one half is always sorted
- Time: O(log n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"This is a rotated sorted array. The minimum is always at the rotation point.
We use binary search, but instead of searching for a target, we identify which
half is properly sorted. The minimum must be in the unsorted half. We narrow
the search space until we find the minimum."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def findMin(self, nums: List[int]) -> int:
        """
        Linear scan - O(n) time.
        """
        return min(nums)


# ─── Optimal ───
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Binary search on rotated sorted array - O(log n) time.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right, min is on the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Min is on the left (including mid)
                right = mid
        
        return nums[left]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard rotated array
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    
    # Test 2: Minimum at start (small rotation)
    assert sol.findMin([2, 1]) == 1
    
    # Test 3: Single element
    assert sol.findMin([1]) == 1
    
    # Test 4: Array rotated to end
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    
    print("All tests passed!")

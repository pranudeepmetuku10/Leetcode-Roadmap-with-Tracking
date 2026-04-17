"""
Problem: Search in Rotated Sorted Array
LeetCode #: 33
Difficulty: Medium
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Pattern: Binary Search
Companies: Microsoft, Amazon, Google, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Linear search through the array
- Time: O(n)  |  Space: O(1)

Optimal:
- Use binary search but adjust for the rotation
- Identify which half is sorted
- If target is in the sorted half, search there
- Otherwise, search in the other half
- Key Insight: One half is always sorted in a rotated array
- Time: O(log n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"In a rotated sorted array, one half is always sorted properly. We find the
sorted half, then check if the target is within that half's range. If yes,
search that half; if not, search the other half. This lets us use binary
search despite the rotation."

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
        Binary search on rotated sorted array - O(log n) time.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Target in left half
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    
    # Test 2: Target in right half
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 4) == 0
    
    # Test 3: Target not found
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # Test 4: Single element found
    assert sol.search([1], 1) == 0
    
    print("All tests passed!")

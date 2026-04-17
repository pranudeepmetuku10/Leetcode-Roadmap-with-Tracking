"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode #: 167
Difficulty: Medium
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Pattern: Two Pointers
Companies: Google, Amazon, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check all pairs of numbers to find target sum
- Time: O(n²)  |  Space: O(1)

Optimal:
- Since array is sorted, use two pointers from start and end
- If sum is too small, move left pointer right
- If sum is too large, move right pointer left
- Key Insight: Sorted array allows pointer movement strategy
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Since the array is sorted, we can use two pointers. Start at both ends,
and if the sum is too small, move the left pointer right to increase sum.
If the sum is too large, move the right pointer left to decrease it.
This is guaranteed to find the target in O(n) time with O(1) space."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Check all pairs - O(n²) time.
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]  # 1-indexed
        return []


# ─── Optimal ───
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Use two pointers on sorted array.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    
    # Test 2: Target at different position
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    
    # Test 3: Negative numbers
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    
    # Test 4: Larger array
    assert sol.twoSum([1, 2, 3, 4, 5, 6, 7], 13) == [6, 7]
    
    print("All tests passed!")

"""
Problem: 3Sum
LeetCode #: 15
Difficulty: Medium
URL: https://leetcode.com/problems/3sum/

Pattern: Two Pointers
Companies: Google, Amazon, Meta, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check all triplets for target sum
- Time: O(n³)  |  Space: O(1)

Optimal:
- Sort array first
- For each element, use two pointers to find complementary pair
- Skip duplicates to avoid duplicate triplets
- Key Insight: Sorting enables two-pointer technique for n-sum
- Time: O(n²)  |  Space: O(1) (excluding sort space)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need three numbers that sum to zero. The brute force is O(n³).
But if we sort first, we can reduce it to O(n²): for each number,
use two pointers to find a pair that completes the target sum.
We skip duplicates to avoid returning the same triplet multiple times."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Check all triplets - O(n³) time.
        """
        n = len(nums)
        result = set()
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return [list(t) for t in result]


# ─── Optimal ───
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort then use two pointers for O(n²) solution.
        """
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Can't possibly sum to 0 if all are positive
            if nums[i] > 0:
                break
            
            # Use two pointers to find complementary pair
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    result = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    assert [-1, -1, 2] in result
    assert [-1, 0, 1] in result
    
    # Test 2: All zeros
    result = sol.threeSum([0, 0, 0, 0])
    assert result == [[0, 0, 0]]
    
    # Test 3: No solution
    result = sol.threeSum([1, 2, -2, -1])
    assert result == []
    
    # Test 4: With duplicates
    result = sol.threeSum([-2, 0, 1, 1, 2])
    assert [-2, 0, 2] in result
    
    print("All tests passed!")

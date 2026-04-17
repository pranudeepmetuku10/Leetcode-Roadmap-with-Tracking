"""
Problem: Two Sum
LeetCode #: 1
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Pattern: HashMap
Companies: Amazon, Google, Microsoft, Meta, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check every pair of numbers to find the target sum
- Time: O(n²)  |  Space: O(1)

Optimal:
- Use a HashMap to store numbers we've seen as we iterate
- For each number, check if (target - number) exists in the map
- Key Insight: Trade space for time by storing values in a lookup table
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT (what to say out loud)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"The problem asks us to find two numbers that sum to a target.
The brute force would be checking all pairs, which is O(n²).
But I notice we can use a HashMap to store values we've seen,
and for each number check if the complement exists. This brings it to O(n)."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Check every pair - O(n²) time.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# ─── Optimal ───
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Use HashMap to find complement in O(n) time.
        """
        seen = {}  # num -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if we've already seen the complement
            if complement in seen:
                return [seen[complement], i]
            
            # Store this number for future lookups
            seen[num] = i
        
        return []


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test 2: Numbers not at start/end
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test 3: Negative numbers
    assert sol.twoSum([3, 3], 6) == [0, 1]
    
    # Test 4: Large target
    assert sol.twoSum([1, 2, 7, 11], 9) == [1, 2]
    
    print("All tests passed!")

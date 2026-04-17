"""
Problem: Contains Duplicate
LeetCode #: 217
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/

Pattern: HashMap
Companies: Amazon, Google, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check every number against every other number
- Time: O(n²)  |  Space: O(1)

Optimal:
- Use a HashSet to track numbers we've seen
- If we see a duplicate, return immediately
- Key Insight: HashSet provides O(1) lookup
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to check if any number appears more than once.
The brute force checks all pairs in O(n²).
But we can use a HashSet to track numbers we've already seen,
and return true as soon as we find a duplicate. This is O(n) time."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check every pair - O(n²) time.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# ─── Optimal ───
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Use HashSet for O(1) lookup.
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


# ─── Optimal (One-liner) ───
class SolutionCompact:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Compare length of list to length of set.
        """
        return len(nums) != len(set(nums))


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Has duplicate
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    
    # Test 2: No duplicate
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    
    # Test 3: All same
    assert sol.containsDuplicate([99, 99]) == True
    
    # Test 4: Single element
    assert sol.containsDuplicate([1]) == False
    
    print("All tests passed!")

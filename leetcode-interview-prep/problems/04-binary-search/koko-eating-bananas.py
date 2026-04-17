"""
Problem: Koko Eating Bananas
LeetCode #: 875
Difficulty: Medium
URL: https://leetcode.com/problems/koko-eating-bananas/

Pattern: Binary Search
Companies: Google, Amazon, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Try every possible eating speed from 1 to max(piles)
- For each speed, calculate time needed
- Time: O(max(piles) * n)  |  Space: O(1)

Optimal:
- Binary search on the eating speed (answer space)
- Left boundary: 1 banana/hour, Right: max(piles)
- For each speed, check if Koko can finish within h hours
- Key Insight: If speed k works, all speeds > k work too (monotonic)
- Time: O(n * log(max(piles)))  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Koko needs to eat all bananas within h hours. The speed range is from 1 to
max(piles). If a speed works, all faster speeds work too - this is monotonic!
We can binary search on the speed. For each candidate speed, we check if she
can finish in time. This is more efficient than trying every speed."

"""
from typing import List
import math


# ─── Brute Force ───
class BruteForceSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Try every speed from 1 to max(piles).
        """
        def canFinish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
        
        for speed in range(1, max(piles) + 1):
            if canFinish(speed):
                return speed
        return max(piles)


# ─── Optimal ───
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search on the eating speed.
        """
        def canFinish(speed: int) -> bool:
            """Check if we can eat all bananas within h hours at this speed."""
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
        
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.minEatingSpeed([1, 1, 1, 1], 4) == 1
    
    # Test 2: Need faster speed
    assert sol.minEatingSpeed([312884132], 968709470) == 1
    
    # Test 3: Multiple piles with tight deadline
    assert sol.minEatingSpeed([1, 10, 1, 1], 4) == 4
    
    # Test 4: Equal piles
    assert sol.minEatingSpeed([1, 1, 1, 1], 4) == 1
    
    print("All tests passed!")

"""
Problem: Non-overlapping Intervals
LeetCode #: 435
Difficulty: Medium
URL: https://leetcode.com/problems/non-overlapping-intervals/

Pattern: Intervals, Greedy
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Try all subsets looking for maximum non-overlapping
- Time: O(2^n)  |  Space: O(n)

Optimal:
- Greedy: sort by end point, pick non-overlapping greedily
- At each step, pick interval with earliest end
- This maximizes room for future intervals
- Key Insight: Earliest end = most intervals can follow
- Time: O(n log n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To maximize non-overlapping intervals, we use greedy: sort by end point,
then pick intervals in order, skipping those that overlap. Picking the
interval with earliest end point leaves the most room for future intervals.
The number of removals = total intervals - maximum non-overlapping."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Generate subsets and find maximum non-overlapping.
        """
        intervals.sort()
        n = len(intervals)
        max_kept = 0
        
        # Try all 2^n subsets
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(intervals[i])
            
            # Check if subset is non-overlapping
            valid = True
            for i in range(len(subset) - 1):
                if subset[i][1] > subset[i + 1][0]:
                    valid = False
                    break
            
            if valid:
                max_kept = max(max_kept, len(subset))
        
        return n - max_kept


# ─── Optimal ───
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy by end point - O(n log n) time.
        """
        # Sort by end point
        intervals.sort(key=lambda x: x[1])
        
        # Keep track of last non-overlapping interval's end
        last_end = intervals[0][1]
        kept = 1
        
        for i in range(1, len(intervals)):
            # If current start >= last end, no overlap
            if intervals[i][0] >= last_end:
                kept += 1
                last_end = intervals[i][1]
        
        return len(intervals) - kept


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Some overlapping
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    
    # Test 2: Multiple overlaps
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    
    # Test 3: Nested intervals
    assert sol.eraseOverlapIntervals([[1, 100], [11, 22], [31, 44], [5, 50]]) == 1
    
    # Test 4: No overlaps
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4]]) == 0
    
    print("All tests passed!")

"""
Problem: Merge Intervals
LeetCode #: 56
Difficulty: Medium
URL: https://leetcode.com/problems/merge-intervals/

Pattern: Intervals, Sorting
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check every pair for overlap, merge if overlapping
- Time: O(n²)  |  Space: O(1)

Optimal:
- Sort intervals by start point
- Iterate and merge consecutive overlapping intervals
- Two intervals overlap if start of next <= end of current
- Key Insight: Sorting makes overlap detection linear
- Time: O(n log n)  |  Space: O(1) or O(n) for output

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To merge intervals, we first sort by start point. Then we iterate through,
checking if the current interval overlaps with the last merged interval. Two
intervals overlap if the current start is within or before the end of the
previous. If they overlap, extend the end. If not, add it as a new interval."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Check all pairs - O(n²) time.
        """
        result = []
        intervals.sort()
        used = [False] * len(intervals)
        
        for i in range(len(intervals)):
            if used[i]:
                continue
            merged = intervals[i][:]
            used[i] = True
            
            for j in range(i + 1, len(intervals)):
                if used[j]:
                    continue
                if merged[1] >= intervals[j][0]:
                    merged[1] = max(merged[1], intervals[j][1])
                    used[j] = True
            
            result.append(merged)
        
        return result


# ─── Optimal ───
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort and merge - O(n log n) time.
        """
        # Sort by start point
        intervals.sort()
        
        result = [intervals[0]]
        
        for current in intervals[1:]:
            last = result[-1]
            
            # Check if current overlaps with last merged
            if current[0] <= last[1]:
                # Merge by extending end
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add as new interval
                result.append(current)
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Some overlapping
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    
    # Test 2: All overlapping
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    
    # Test 3: No overlapping
    assert sol.merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    
    # Test 4: Single interval
    assert sol.merge([[1]]) == [[1]]
    
    print("All tests passed!")

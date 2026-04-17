"""
Problem: Meeting Rooms II
LeetCode #: 253
Difficulty: Medium
URL: https://leetcode.com/problems/meeting-rooms-ii/

Pattern: Intervals, Heap
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- For each meeting, check all rooms for overlaps
- Time: O(n²)  |  Space: O(n)

Optimal:
- Sort meetings by start time
- Use min-heap to track room end times
- For each meeting, check if earliest room is free
- Key Insight: Earliest available room has earliest end time
- Time: O(n log n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To find minimum meeting rooms, we sort meetings by start time. We use a
min-heap to track when each room becomes free. For each meeting, if the
earliest available room is free before this meeting starts, we reuse it.
Otherwise, we need a new room. The heap size is the answer."

"""
from typing import List
import heapq


# ─── Brute Force ───
class BruteForceSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Check each meeting against all rooms - O(n²) time.
        """
        if not intervals:
            return 0
        
        intervals.sort()
        rooms = []  # List of room end times
        
        for start, end in intervals:
            # Find a room that's free
            found = False
            for i in range(len(rooms)):
                if rooms[i] <= start:
                    rooms[i] = end
                    found = True
                    break
            
            if not found:
                rooms.append(end)
        
        return len(rooms)


# ─── Optimal ───
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Min-heap tracking room end times - O(n log n) time.
        """
        if not intervals:
            return 0
        
        # Sort meetings by start time
        intervals.sort()
        
        # Min-heap of room end times
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        
        for start, end in intervals[1:]:
            # If earliest room is available, reuse it
            if rooms[0] <= start:
                heapq.heappop(rooms)
            
            # Add this meeting to a room
            heapq.heappush(rooms, end)
        
        return len(rooms)


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple overlapping meetings
    assert sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    
    # Test 2: No overlaps
    assert sol.minMeetingRooms([[7, 10], [2, 4]]) == 1
    
    # Test 3: All overlapping
    assert sol.minMeetingRooms([[1, 5], [1, 5], [1, 5]]) == 3
    
    # Test 4: Back-to-back meetings (no overlap at boundaries)
    assert sol.minMeetingRooms([[1, 2], [2, 3], [3, 4]]) == 1
    
    print("All tests passed!")

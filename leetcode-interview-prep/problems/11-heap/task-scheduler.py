"""
Problem: Task Scheduler
LeetCode #: 621
Difficulty: Medium
URL: https://leetcode.com/problems/task-scheduler/

Pattern: Heap, Greedy
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Greedy simulation: pick most frequent task available
- Time: O(n log 26)  |  Space: O(26)

Optimal:
- Calculate mathematically using max frequency
- Min slots = (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
- Key Insight: Bottleneck is most frequent task
- Time: O(n)  |  Space: O(26)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"The constraint is that the most frequent task determines the schedule. If
a task appears f times with cooldown n, we need at least (f-1)*(n+1) slots
plus 1 for the final task. We can calculate this directly without simulating.
Other tasks fill the gaps between instances of the most frequent task."

"""
from typing import List
from collections import Counter
import heapq


# ─── Brute Force ───
class BruteForceSolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Greedy simulation with heap - O(n log 26) time.
        """
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while max_heap:
            cycle = []
            # Try to schedule n+1 tasks
            for i in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    cycle.append(count)
                time += 1
            
            # Put back tasks that need rescheduling
            for count in cycle:
                if count + 1 < 0:  # Count is negative
                    heapq.heappush(max_heap, count + 1)
            
            # Subtract idle time from last partial cycle
            if max_heap:
                time -= n + 1 - len(cycle)
        
        return time


# ─── Optimal ───
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Mathematical formula - O(n) time.
        """
        task_counts = Counter(tasks)
        
        # Find maximum frequency
        max_freq = max(task_counts.values())
        
        # Count how many tasks have maximum frequency
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Minimum time = (max_freq - 1) * (n + 1) + max_freq_count
        # But at least len(tasks) if tasks fill all space
        min_time = (max_freq - 1) * (n + 1) + max_freq_count
        return max(min_time, len(tasks))


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    
    # Test 2: Single task
    assert sol.leastInterval(["A"], 2) == 1
    
    # Test 3: No cooldown needed
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    
    # Test 4: Mixed frequencies
    assert sol.leastInterval(["A", "A", "A", "B", "B", "C", "C"], 2) == 9
    
    print("All tests passed!")

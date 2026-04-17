"""
Problem: Rotting Oranges
LeetCode #: 994
Difficulty: Medium
URL: https://leetcode.com/problems/rotting-oranges/

Pattern: Graphs, BFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Simulate rotting by level, track max level
- Time: O(m*n*k) where k is time  |  Space: O(m*n)

Optimal:
- BFS from all rotten oranges simultaneously
- Rotten orange spreads to adjacent fresh oranges each minute
- Return time when all oranges are rotten
- Key Insight: Multi-source BFS for spreading
- Time: O(m*n)  |  Space: O(m*n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Rotting spreads to adjacent oranges each minute. This is a multi-source BFS
problem. We start BFS from all initially rotten oranges simultaneously. As
we process each orange, its neighbors become rotten in the next minute. We
track the maximum time seen. If fresh oranges remain, return -1."

"""
from typing import List
from collections import deque


# ─── Brute Force ───
class BruteForceSolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Simulate rotting level by level.
        """
        rows, cols = len(grid), len(grid[0])
        time = 0
        
        while True:
            rotten_this_round = []
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                                rotten_this_round.append((ni, nj))
            
            if not rotten_this_round:
                break
            
            for i, j in rotten_this_round:
                grid[i][j] = 2
            time += 1
        
        # Check if any fresh oranges remain
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return time


# ─── Optimal ───
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS - O(m*n) time.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all rotten oranges and count fresh
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # BFS from all rotten oranges
        max_time = 0
        while queue:
            row, col, time = queue.popleft()
            max_time = max(max_time, time)
            
            # Spread to adjacent cells
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the orange
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
        
        # If any fresh oranges remain, impossible
        return max_time if fresh_count == 0 else -1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert sol.orangesRotting([row[:] for row in grid1]) == 4
    
    # Test 2: All rotten
    grid2 = [[2, 2], [2, 2]]
    assert sol.orangesRotting([row[:] for row in grid2]) == 0
    
    # Test 3: No fresh oranges
    grid3 = [[0, 2]]
    assert sol.orangesRotting([row[:] for row in grid3]) == 0
    
    # Test 4: Fresh orange isolated
    grid4 = [[2, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert sol.orangesRotting([row[:] for row in grid4]) == -1
    
    print("All tests passed!")

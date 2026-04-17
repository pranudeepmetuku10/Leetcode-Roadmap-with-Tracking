"""
Problem: Number of Islands
LeetCode #: 200
Difficulty: Medium
URL: https://leetcode.com/problems/number-of-islands/

Pattern: Graphs, DFS/BFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Count connected components using BFS from each unvisited '1'
- Time: O(m*n)  |  Space: O(m*n)

Optimal:
- DFS or BFS to mark all connected land as visited
- Increment counter for each new island found
- Key Insight: Mark cells as visited to avoid recounting
- Time: O(m*n)  |  Space: O(m*n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We count islands by finding connected components of '1' cells. We iterate
through the grid. When we find an unvisited '1', we start a DFS/BFS to mark
all connected cells as visited and increment the island count. After
processing all cells, we have the total number of islands."

"""
from typing import List
from collections import deque


# ─── Brute Force ───
class BruteForceSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Simple DFS approach.
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Mark as visited
            grid[r][c] = '0'
            # Explore neighbors
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    dfs(nr, nc)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count


# ─── Optimal ───
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS to explore connected components - O(m*n) time.
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            """Mark all connected land as visited."""
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            
            # Mark as visited
            grid[r][c] = '0'
            
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count


# ─── Test Cases ───
if __name__ == "__main__":
    # Test 1: Multiple islands
    grid1 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    sol = Solution()
    assert sol.numIslands([row[:] for row in grid1]) == 3
    
    # Test 2: Single island
    grid2 = [["1", "1", "1"],
             ["0", "1", "0"],
             ["1", "1", "1"]]
    assert sol.numIslands([row[:] for row in grid2]) == 1
    
    # Test 3: No islands
    grid3 = [["0", "0"],
             ["0", "0"]]
    assert sol.numIslands([row[:] for row in grid3]) == 0
    
    # Test 4: All islands
    grid4 = [["1", "1"],
             ["1", "1"]]
    assert sol.numIslands([row[:] for row in grid4]) == 1
    
    print("All tests passed!")

"""
Problem: Pacific Atlantic Water Flow
LeetCode #: 417
Difficulty: Medium
URL: https://leetcode.com/problems/pacific-atlantic-water-flow/

Pattern: Graphs, DFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- For each cell, check if it can reach both oceans
- Time: O((m*n)²)  |  Space: O(m*n)

Optimal:
- Reverse thinking: start from oceans, see which cells they reach
- DFS from all Pacific border cells, DFS from all Atlantic border cells
- Cells reachable from both are valid
- Key Insight: Water flows DOWN (<=), so reverse is UP (>=)
- Time: O(m*n)  |  Space: O(m*n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"A cell flows to an ocean if water can flow downhill from that cell to the
ocean. Instead of checking each cell, we reverse the problem: start from
ocean borders and work backward to find all cells that can reach each ocean
(water flows uphill in reverse). Cells reachable from both are the answer."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Check each cell - O((m*n)²) time.
        """
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        result = []
        
        def can_reach(r, c, ocean_set):
            visited = set()
            stack = [(r, c)]
            while stack:
                row, col = stack.pop()
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                if (row, col) in ocean_set:
                    return True
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in visited and heights[nr][nc] >= heights[row][col]:
                            stack.append((nr, nc))
            return False
        
        pacific = set()
        for i in range(rows):
            pacific.add((i, 0))
        for j in range(cols):
            pacific.add((0, j))
        
        atlantic = set()
        for i in range(rows):
            atlantic.add((i, cols - 1))
        for j in range(cols):
            atlantic.add((rows - 1, j))
        
        for i in range(rows):
            for j in range(cols):
                if can_reach(i, j, pacific) and can_reach(i, j, atlantic):
                    result.append([i, j])
        
        return result


# ─── Optimal ───
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Reverse DFS from oceans - O(m*n) time.
        """
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            """Mark all cells reachable from (r, c) going uphill."""
            if (r, c) in visited:
                return
            visited.add((r, c))
            
            # Check all 4 neighbors
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # Can flow uphill (from neighbor if it's >= current height)
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        # DFS from Pacific border (top and left)
        for i in range(rows):
            dfs(i, 0, pacific)  # Left edge
        for j in range(cols):
            dfs(0, j, pacific)  # Top edge
        
        # DFS from Atlantic border (bottom and right)
        for i in range(rows):
            dfs(i, cols - 1, atlantic)  # Right edge
        for j in range(cols):
            dfs(rows - 1, j, atlantic)  # Bottom edge
        
        # Cells reachable from both
        return [[r, c] for r in range(rows) for c in range(cols) 
                if (r, c) in pacific and (r, c) in atlantic]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    heights1 = [[4, 2, 7, 6],
                [9, 4, 8, 1],
                [4, 7, 2, 1]]
    result1 = sol.pacificAtlantic(heights1)
    assert [0, 2] in result1
    assert [1, 0] in result1
    
    # Test 2: 1x1 grid
    heights2 = [[1]]
    result2 = sol.pacificAtlantic(heights2)
    assert result2 == [[0, 0]]
    
    # Test 3: All same height
    heights3 = [[1, 1], [1, 1]]
    result3 = sol.pacificAtlantic(heights3)
    assert len(result3) == 4
    
    # Test 4: Diagonal flow
    heights4 = [[1, 2, 3],
                [8, 9, 4],
                [7, 6, 5]]
    result4 = sol.pacificAtlantic(heights4)
    assert len(result4) > 0
    
    print("All tests passed!")

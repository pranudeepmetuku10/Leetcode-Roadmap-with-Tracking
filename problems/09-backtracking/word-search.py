"""
Problem: Word Search
LeetCode #: 79
Difficulty: Medium
URL: https://leetcode.com/problems/word-search/

Pattern: Backtracking
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- From each cell, try DFS if it matches first character
- Time: O(m*n*4^L) where L=word length  |  Space: O(L)

Optimal:
- DFS with backtracking from each cell
- Mark visited cells with a sentinel
- Track character index in word
- Key Insight: In-place marking avoids extra space for visited set
- Time: O(m*n*4^L)  |  Space: O(L) for recursion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To search for a word in a grid, we use DFS from each cell. We check if the
current cell matches the current character in the word. If it does, we
recursively search neighbors. We mark cells as visited by temporarily
changing the character, then restore it for backtracking."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS with visited set.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index, visited):
            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
            
            result = (dfs(r + 1, c, index + 1, visited) or
                     dfs(r - 1, c, index + 1, visited) or
                     dfs(r, c + 1, index + 1, visited) or
                     dfs(r, c - 1, index + 1, visited))
            
            visited.remove((r, c))
            return result
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        
        return False


# ─── Optimal ───
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS with in-place marking - O(m*n*4^L) time.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Found the entire word
            if index == len(word):
                return True
            
            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # Cell already visited or character doesn't match
            if board[r][c] == '#' or board[r][c] != word[index]:
                return False
            
            # Mark as visited
            board[r][c] = '#'
            
            # Search in 4 directions
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            # Backtrack
            board[r][c] = word[index]
            
            return found
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Word exists
    board1 = [["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]]
    assert sol.exist([row[:] for row in board1], "ABCCED") == True
    
    # Test 2: Word exists with reuse
    assert sol.exist([row[:] for row in board1], "SEE") == True
    
    # Test 3: Word doesn't exist
    assert sol.exist([row[:] for row in board1], "ABCB") == False
    
    # Test 4: Single character
    board4 = [["A"]]
    assert sol.exist([row[:] for row in board4], "A") == True
    
    print("All tests passed!")

"""
Problem: Search a 2D Matrix
LeetCode #: 74
Difficulty: Medium
URL: https://leetcode.com/problems/search-a-2d-matrix/

Pattern: Binary Search
Companies: Microsoft, Amazon, Google, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check every element in the 2D matrix
- Time: O(m*n)  |  Space: O(1)

Optimal:
- Treat 2D matrix as a 1D sorted array
- Use binary search on the conceptual 1D array
- Convert 1D index to 2D coordinates: row = mid // cols, col = mid % cols
- Key Insight: Matrix is sorted both row-wise and column-wise
- Time: O(log(m*n))  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"This 2D matrix is sorted both by rows and columns, so we can treat it
as a single sorted 1D array. We apply binary search on this virtual sorted
array, and convert the 1D index back to 2D coordinates. This reduces the
time to O(log(m*n)) while keeping space O(1)."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Check every element - O(m*n) time.
        """
        for row in matrix:
            if target in row:
                return True
        return False


# ─── Optimal ───
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search treating 2D matrix as 1D sorted array.
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Target found in matrix
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    
    # Test 2: Target not found
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
    
    # Test 3: Single row
    assert sol.searchMatrix([[1]], 1) == True
    
    # Test 4: Target at end
    assert sol.searchMatrix([[1, 3], [5, 7]], 7) == True
    
    print("All tests passed!")

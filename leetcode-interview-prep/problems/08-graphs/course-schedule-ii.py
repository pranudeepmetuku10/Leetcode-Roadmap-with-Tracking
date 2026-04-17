"""
Problem: Course Schedule II
LeetCode #: 210
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule-ii/

Pattern: Graphs, Topological Sort
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- DFS cycle detection + topological sort
- Time: O(n + e)  |  Space: O(n + e)

Optimal:
- Kahn's algorithm (BFS topological sort with in-degrees)
- Remove nodes with in-degree 0, update neighbors
- If all nodes processed, valid ordering exists
- Key Insight: In-degree approach is intuitive for ordering
- Time: O(n + e)  |  Space: O(n + e)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"This requires both cycle detection and a valid ordering. We use Kahn's
algorithm: track in-degree of each node. Nodes with in-degree 0 can be
taken first. Remove them and decrease neighbors' in-degrees. Repeat until
no more nodes with in-degree 0. If we processed all nodes, a valid order
exists."

"""
from typing import List
from collections import defaultdict, deque


# ─── Brute Force ───
class BruteForceSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS topological sort.
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        order = []
        
        def dfs(course):
            if state[course] == 1:
                return False  # Cycle detected
            if state[course] == 2:
                return True  # Already processed
            
            state[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            order.append(course)
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []
        
        return order


# ─── Optimal ───
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Kahn's algorithm (BFS topological sort) - O(n+e) time.
        """
        # Build graph and in-degree map
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Find all nodes with in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            # Decrease in-degree of neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all courses are in order, valid; else cycle exists
        return order if len(order) == numCourses else []


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid order exists
    result1 = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert len(result1) == 4
    # Verify order: 0 before 1, 0 before 2, 1 before 3, 2 before 3
    assert result1.index(0) < result1.index(1)
    assert result1.index(0) < result1.index(2)
    
    # Test 2: Cycle exists
    result2 = sol.findOrder(2, [[1, 0], [0, 1]])
    assert result2 == []
    
    # Test 3: No prerequisites
    result3 = sol.findOrder(3, [])
    assert len(result3) == 3
    
    # Test 4: Single course
    result4 = sol.findOrder(1, [])
    assert result4 == [0]
    
    print("All tests passed!")

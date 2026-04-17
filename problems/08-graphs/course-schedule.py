"""
Problem: Course Schedule
LeetCode #: 207
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule/

Pattern: Graphs, Topological Sort
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- DFS from each course, check for cycles
- Time: O(n² + e)  |  Space: O(n + e)

Optimal:
- Topological sort using DFS with state tracking
- States: unvisited (0), visiting (1), visited (2)
- If we revisit a 'visiting' node, there's a cycle
- Key Insight: Cycle exists iff we can't finish topological sort
- Time: O(n + e)  |  Space: O(n + e)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to detect if prerequisites form a cycle. We can use DFS with state
tracking. States are: unvisited (0), currently visiting (1), visited (2). If
we encounter a node that's currently being visited, we found a cycle. We
build the graph from prerequisites and check for cycles."

"""
from typing import List
from collections import defaultdict


# ─── Brute Force ───
class BruteForceSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Check each node for cycles.
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def has_cycle(node, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(node)
            return False
        
        visited = set()
        for course in range(numCourses):
            if course not in visited:
                if has_cycle(course, visited, set()):
                    return False
        return True


# ─── Optimal ───
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS with state tracking for cycle detection - O(n+e) time.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 1:
                # Currently visiting - found a cycle
                return True
            if state[course] == 2:
                # Already visited
                return False
            
            # Mark as visiting
            state[course] = 1
            
            # Check all neighbors
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            # Mark as visited (finished)
            state[course] = 2
            return False
        
        # Check each course
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: No cycle
    assert sol.canFinish(2, [[1, 0]]) == True
    
    # Test 2: Cycle exists
    assert sol.canFinish(2, [[1, 0], [0, 1]]) == False
    
    # Test 3: No prerequisites
    assert sol.canFinish(3, []) == True
    
    # Test 4: Chain without cycle
    assert sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]) == True
    
    print("All tests passed!")

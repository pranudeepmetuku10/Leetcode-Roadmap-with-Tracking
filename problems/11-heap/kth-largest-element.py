"""
Problem: Kth Largest Element in an Array
LeetCode #: 215
Difficulty: Medium
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Pattern: Heap
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Sort array, return k-th element
- Time: O(n log n)  |  Space: O(1)

Optimal:
- Use min-heap of size k
- Maintain heap with k largest elements
- When heap > k, pop smallest
- Final heap top is kth largest
- Key Insight: Heap maintains k best elements efficiently
- Time: O(n log k)  |  Space: O(k)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To find the kth largest element, we can sort (O(n log n)) or use a heap
(O(n log k)). We maintain a min-heap of size k containing the k largest
elements. As we process elements, if the heap exceeds k elements, we remove
the smallest. The top of the heap is the kth largest."

"""
from typing import List
import heapq


# ─── Brute Force ───
class BruteForceSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Sort and return k-th element - O(n log n) time.
        """
        nums.sort(reverse=True)
        return nums[k - 1]


# ─── Optimal ───
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Min-heap of size k - O(n log k) time.
        """
        # Min-heap to keep track of k largest elements
        min_heap = []
        
        for num in nums:
            # Add current number
            heapq.heappush(min_heap, num)
            
            # Keep only k largest
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Root of min-heap is kth largest
        return min_heap[0]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    
    # Test 2: k=1 (largest)
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 1) == 6
    
    # Test 3: Negative numbers
    assert sol.findKthLargest([1], 1) == 1
    
    # Test 4: Duplicates
    assert sol.findKthLargest([99, 99], 2) == 99
    
    print("All tests passed!")

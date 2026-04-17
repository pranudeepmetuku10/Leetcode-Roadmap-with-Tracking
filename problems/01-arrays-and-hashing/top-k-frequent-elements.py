"""
Problem: Top K Frequent Elements
LeetCode #: 347
Difficulty: Medium
URL: https://leetcode.com/problems/top-k-frequent-elements/

Pattern: HashMap + Heap
Companies: Google, Amazon, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Count frequencies, sort by frequency, return top k
- Time: O(n log n)  |  Space: O(n)

Optimal:
- Count frequencies with HashMap
- Use a min heap of size k to track top k elements
- Process frequencies in O(n log k) time
- Key Insight: Heap keeps only top k, more efficient than full sort
- Time: O(n log k)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to find k most frequent elements. First, count frequencies
using a HashMap. Then we use a min heap of size k to track the top k
elements. As we process each frequency, we maintain the heap so it always
contains the k largest frequencies. This is O(n log k) time."

"""
import heapq
from typing import List
from collections import Counter


# ─── Brute Force ───
class BruteForceSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Count frequencies, sort, return top k.
        """
        from collections import Counter
        
        freq = Counter(nums)
        # Sort by frequency (descending) and take top k
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]


# ─── Optimal (Heap) ───
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Use min heap of size k for O(n log k) solution.
        """
        if k == len(set(nums)):
            return list(set(nums))
        
        # Count frequencies
        freq = Counter(nums)
        
        # Use max heap (negate values for Python's min heap)
        # Keep track of (frequency, element)
        heap = [(-frequency, num) for num, frequency in freq.items()]
        heapq.heapify(heap)
        
        # Extract top k
        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)
        
        return result


# ─── Optimal (Min Heap) ───
class SolutionMinHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Maintain min heap of size k - more efficient for large n.
        """
        freq = Counter(nums)
        
        # Min heap: keep only top k frequent elements
        min_heap = []
        
        for num, frequency in freq.items():
            heapq.heappush(min_heap, (frequency, num))
            
            # Keep heap size at most k
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Extract elements from heap
        return [num for frequency, num in min_heap]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    result = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]
    
    # Test 2: Single element
    result = sol.topKFrequent([1], 1)
    assert result == [1]
    
    # Test 3: k equals number of unique elements
    result = sol.topKFrequent([4, 1, 1, -1, -3], 2)
    assert len(result) == 2 and 1 in result
    
    # Test 4: All frequencies are same
    result = sol.topKFrequent([1, 2, 3], 2)
    assert len(result) == 2
    
    print("All tests passed!")

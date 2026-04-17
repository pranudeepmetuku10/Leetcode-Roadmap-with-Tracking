"""
Problem: Find Median from Data Stream
LeetCode #: 295
Difficulty: Hard
URL: https://leetcode.com/problems/find-median-from-data-stream/

Pattern: Heap
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Store all numbers, sort on each query
- Time: O(n log n) per query  |  Space: O(n)

Optimal:
- Use two heaps: max-heap for smaller half, min-heap for larger half
- Keep sizes roughly equal
- Median is top of max-heap or average of both tops
- Key Insight: Two heaps maintain sorted property dynamically
- Time: O(log n) add, O(1) query  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To find median dynamically, we use two heaps. The max-heap stores the smaller
half (we negate values since Python has min-heap), and the min-heap stores the
larger half. We keep them balanced so the larger heap has at most 1 more
element. The median is either from the larger heap or the average of both."

"""
import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize two heaps:
        - small: max-heap of smaller half (using negated values)
        - large: min-heap of larger half
        """
        self.small = []  # Max-heap (negated)
        self.large = []  # Min-heap


# ─── Brute Force ───
class BruteForceSolution:
    def __init__(self):
        self.nums = []
    
    def addNum(self, num: int) -> None:
        self.nums.append(num)
    
    def findMedian(self) -> float:
        """Find median by sorting - O(n log n) time."""
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        if n % 2 == 1:
            return float(sorted_nums[n // 2])
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2.0


# ─── Optimal ───
class Solution:
    def __init__(self):
        """
        Two heaps: max-heap for smaller half, min-heap for larger half.
        """
        self.small = []  # Max-heap (negated values)
        self.large = []  # Min-heap
    
    def addNum(self, num: int) -> None:
        """Add number while maintaining heap properties - O(log n) time."""
        # Always add to max-heap first (negated)
        heapq.heappush(self.small, -num)
        
        # Ensure every element in max-heap <= every element in min-heap
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance: small can have at most 1 more than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self) -> float:
        """Find median - O(1) time."""
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# ─── Test Cases ───
if __name__ == "__main__":
    mf = Solution()
    
    # Test 1: Build stream [1,2]
    mf.addNum(1)
    assert mf.findMedian() == 1.0
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    
    # Test 2: Add more numbers
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    
    # Test 3: Larger stream
    mf2 = Solution()
    for num in [5, 15, 1, 3]:
        mf2.addNum(num)
    assert mf2.findMedian() == 4.0
    
    # Test 4: Single number
    mf3 = Solution()
    mf3.addNum(1)
    assert mf3.findMedian() == 1.0
    
    print("All tests passed!")

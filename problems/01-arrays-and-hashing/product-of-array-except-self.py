"""
Problem: Product of Array Except Self
LeetCode #: 238
Difficulty: Medium
URL: https://leetcode.com/problems/product-of-array-except-self/

Pattern: Arrays
Companies: Google, Amazon, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- For each position, multiply all other elements
- Naive if using division: O(n) but must handle zeros
- Time: O(n²)  |  Space: O(1)

Optimal:
- Use prefix and suffix products
- prefix[i] = product of all elements to the left
- suffix[i] = product of all elements to the right
- result[i] = prefix[i] × suffix[i]
- Key Insight: Avoid division by building left and right products
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need the product of all elements except self at each position.
We can't just divide because of zeros. Instead, we use prefix and suffix
products: for each position, multiply the product of all elements to the
left with the product of all elements to the right. This is O(n) time."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        For each position, multiply all elements except that position.
        """
        n = len(nums)
        result = []
        
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result.append(product)
        
        return result


# ─── Optimal (Prefix-Suffix) ───
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Use prefix and suffix products.
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        
        # Build prefix array: prefix[i] = product of all elements to the left
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Build suffix array: suffix[i] = product of all elements to the right
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # result[i] = left product × right product
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result


# ─── Optimal (O(1) space) ───
class SolutionSpaceOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Use only result array, no extra space for prefix/suffix.
        """
        n = len(nums)
        result = [1] * n
        
        # First pass: build prefix products in result
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Second pass: multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal case
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test 2: With zero
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    # Test 3: Small array
    assert sol.productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24]
    
    # Test 4: Two elements
    assert sol.productExceptSelf([1, 2]) == [2, 1]
    
    print("All tests passed!")

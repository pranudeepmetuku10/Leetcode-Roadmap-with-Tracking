"""
Problem: Group Anagrams
LeetCode #: 49
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

Pattern: HashMap
Companies: Google, Meta, Microsoft, Amazon

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Sort each string and compare all pairs
- Time: O(n² × m log m) where m is max string length

Optimal:
- Use sorted string as key in HashMap: all anagrams have same sorted form
- Group strings by their sorted key
- Key Insight: Anagrams produce identical strings when sorted
- Time: O(n × m log m)  |  Space: O(n × m)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to group anagrams together. The key insight is that anagrams
have the same characters when sorted. So we can use the sorted string
as a key in a HashMap to group all anagrams with the same sorted form.
This is O(n × m log m) where m is the string length."

"""
from typing import List
from collections import defaultdict


# ─── Brute Force ───
class BruteForceSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Compare all strings with all other strings.
        """
        result = []
        used = set()
        
        for i, s in enumerate(strs):
            if i in used:
                continue
            
            group = [s]
            for j in range(i + 1, len(strs)):
                if j not in used and sorted(s) == sorted(strs[j]):
                    group.append(strs[j])
                    used.add(j)
            
            result.append(group)
        
        return result


# ─── Optimal ───
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group by sorted string as key.
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# ─── Optimal (using count key) ───
class SolutionCountKey:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use character count as key instead of sorting.
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count characters: create a tuple key
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple groups
    result = sol.groupAnagrams(["eat", "tea", "ate", "eat", "tan", "nat", "bat"])
    assert len(result) == 3
    
    # Test 2: Single group
    result = sol.groupAnagrams([""])
    assert result == [[""]]
    
    # Test 3: All same anagram group
    result = sol.groupAnagrams(["a"])
    assert result == [["a"]]
    
    # Test 4: Non-anagrams
    result = sol.groupAnagrams(["ab", "ba", "abc"])
    assert len(result) == 2
    
    print("All tests passed!")

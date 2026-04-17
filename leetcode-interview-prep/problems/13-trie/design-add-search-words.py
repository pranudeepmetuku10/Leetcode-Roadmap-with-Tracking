"""
Problem: Design Add and Search Words Data Structure
LeetCode #: 211
Difficulty: Medium
URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Pattern: Trie, DFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Store words in list, search with regex or pattern matching
- Time: O(n*m) for search  |  Space: O(n*m)

Optimal:
- Trie structure with wildcard support via DFS
- '.' can match any single character
- Use DFS to explore all possible matches
- Key Insight: Trie + DFS enables efficient wildcard matching
- Time: O(m*26^m) worst case  |  Space: O(n*m)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We build on the Trie structure but add support for wildcards. The '.' can
match any character. In search, when we encounter a '.', we try all 26
child paths using DFS. This explores all possible interpretations of the
wildcard and returns true if any path leads to a word end."

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# ─── Brute Force ───
class BruteForceWordDictionary:
    def __init__(self):
        self.words = set()
    
    def addWord(self, word: str) -> None:
        self.words.add(word)
    
    def search(self, word: str) -> bool:
        """Pattern matching with wildcards - O(n*m) time."""
        import re
        pattern = word.replace(".", ".")  # '.' is already regex wildcard
        for w in self.words:
            if re.fullmatch(pattern, w):
                return True
        return False


# ─── Optimal ───
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Add word - O(m) time."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search with wildcard support - O(m*26^m) worst case."""
        def dfs(node, index):
            # Reached end of word pattern
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
            
            if char == ".":
                # Try all possible characters
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # Exact character match
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)


# ─── Test Cases ───
if __name__ == "__main__":
    wd = WordDictionary()
    
    # Test 1: Basic add and search
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    
    # Test 2: Wildcard at different positions
    wd2 = WordDictionary()
    wd2.addWord("hello")
    assert wd2.search("hello") == True
    assert wd2.search("h....") == True
    assert wd2.search(".ello") == True
    assert wd2.search("he...") == True
    assert wd2.search("world") == False
    
    # Test 3: Multiple wildcards
    wd3 = WordDictionary()
    wd3.addWord("cat")
    wd3.addWord("bat")
    assert wd3.search("...") == True
    assert wd3.search(".at") == True
    
    # Test 4: No matches
    wd4 = WordDictionary()
    wd4.addWord("abc")
    assert wd4.search("...d") == False
    
    print("All tests passed!")

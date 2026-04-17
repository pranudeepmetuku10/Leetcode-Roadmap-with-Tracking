"""
Problem: Implement Trie (Prefix Tree)
LeetCode #: 208
Difficulty: Medium
URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Pattern: Trie, Design
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Store words in a list
- Search involves linear scanning
- Time: O(n*m) for search  |  Space: O(n*m)

Optimal:
- Tree structure: each node has children for each letter
- Each node tracks if it's end of word
- Search/Insert: O(m) where m is word length
- Key Insight: Prefix sharing reduces space and time
- Time: O(m) insert/search  |  Space: O(m*n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"A Trie is a tree where each node represents a character. We insert words
character by character, creating nodes as needed. For search, we traverse
following the characters. Each node tracks if it's the end of a word.
Prefix search finds all nodes along a path without needing the end marker."

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# ─── Brute Force ───
class BruteForceTrie:
    def __init__(self):
        self.words = set()
    
    def insert(self, word: str) -> None:
        self.words.add(word)
    
    def search(self, word: str) -> bool:
        return word in self.words
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with prefix - O(n*m) time."""
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False


# ─── Optimal ───
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word - O(m) time."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for exact word - O(m) time."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with prefix - O(m) time."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# ─── Test Cases ───
if __name__ == "__main__":
    trie = Trie()
    
    # Test 1: Basic insert and search
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.search("appl") == False
    
    # Test 2: Prefix search
    trie.insert("app")
    assert trie.startsWith("app") == True
    assert trie.search("app") == True
    
    # Test 3: Multiple words
    trie2 = Trie()
    trie2.insert("car")
    trie2.insert("card")
    assert trie2.search("car") == True
    assert trie2.search("card") == True
    assert trie2.startsWith("ca") == True
    
    # Test 4: No match
    trie3 = Trie()
    trie3.insert("hello")
    assert trie3.search("world") == False
    assert trie3.startsWith("world") == False
    
    print("All tests passed!")

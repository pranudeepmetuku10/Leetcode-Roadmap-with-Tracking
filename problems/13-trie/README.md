# Trie

## Pattern Overview

Trie (prefix tree) efficiently stores and retrieves strings. Ideal for prefix matching, autocomplete, and word problems.

## When to Recognize This Pattern

**Trigger words:**
- "Prefix matching"
- "Autocomplete"
- "Word search in dictionary"
- "Implement dictionary"
- "Wildcard matching"

## Template/Pseudocode

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| Prefix search | O(m) | O(1) |
| Space total | O(n * m) | O(1) |

Where m = word length, n = number of words

## Common Mistakes to Avoid

1. **Confusing search and startsWith** — Search checks full word, startsWith checks prefix
2. **Not marking word end** — Multiple words can share prefixes
3. **Returning node not bool** — Call startsWith not returning the node
4. **Memory waste** — Trie uses more space than HashMap for small sets
5. **Edge cases** — Empty string, single character, very long words

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Implement Trie | Medium | 208 |
| Design Add & Search Words | Medium | 211 |

## Key Insights

- **Prefix tree structure** — Shares common prefixes efficiently
- **Time complexity** — O(m) not O(n), where m is word length
- **Space tradeoff** — More memory than HashSet but faster prefix queries
- **Wildcard matching** — Use DFS with `.` wildcard support
- **AutoComplete** — DFS from node to find all words with prefix

## Related Patterns

- **HashMap** — Simple alternative for exact word search
- **DFS** — For exploring all words with prefix
- **BFS** — Breadth-first word exploration

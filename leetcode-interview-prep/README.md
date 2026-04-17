# 🔥 LeetCode Interview Prep — 8-Week MAANG + Mid-Level Roadmap

> **Structured coding interview preparation for MAANG + mid-level tech companies**  
> 76 curated problems | 13 core patterns | 8 weeks | Production-ready solutions | Mock interview templates

![Problems](https://img.shields.io/badge/Problems-76-brightgreen) ![Patterns](https://img.shields.io/badge/Patterns-13-blue) ![Duration](https://img.shields.io/badge/Duration-8%20Weeks-orange) ![Difficulty](https://img.shields.io/badge/Difficulty-Easy%20%7C%20Medium%20%7C%20Hard-red)

## 📋 8-Week Roadmap Overview

| Week | Pattern Focus | Problems | Easy | Medium | Hard | Focus |
|------|---------------|----------|------|--------|------|-------|
| **1** | Arrays & Hashing + Two Pointers | 10 | 4 | 6 | — | Fundamentals |
| **2** | Sliding Window + Binary Search | 10 | 2 | 8 | — | Optimization |
| **3** | Stack + Linked Lists | 10 | 4 | 5 | 1 | Data Structures |
| **4** | Trees — BFS/DFS | 10 | 3 | 5 | 2 | Traversal |
| **5** | Graphs + Backtracking | 9 | — | 8 | 1 | Exploration |
| **6** | Dynamic Programming | 9 | 1 | 8 | — | Optimization |
| **7** | Heap + Intervals + Trie | 9 | — | 7 | 2 | Advanced DS |
| **8** | Mixed Review + Mock Interviews | 9 | — | 8 | 1 | Integration |
| — | **TOTAL** | **76** | **18** | **55** | **7** | |

## 🎯 Pattern Quick Reference

| Pattern | When to Use | Example |  Time | Space |
|---------|----------|---------|--------|--------|
| **Two Pointers** | Sorted array, pairs, palindromes | 3Sum | O(n²) | O(1) |
| **Sliding Window** | Subarrays, fixed/variable window | Min Window | O(n) | O(k) |
| **Binary Search** | Sorted data, search space halving | Koko Eating | O(log n) | O(1) |
| **HashMap** | Lookup, frequency, grouping | Two Sum | O(n) | O(n) |
| **Stack** | Matching pairs, Next Greater | Daily Temps | O(n) | O(n) |
| **BFS/DFS** | Traversal, connectivity | Number Islands | O(V+E) | O(V) |
| **Backtracking** | All solutions, combinations | Subsets | O(2^n) | O(n) |
| **DP (1D)** | Optimization, state tracking | Coin Change | O(n×m) | O(n) |
| **DP (2D)** | Grid problems, 2D states | Unique Paths | O(m×n) | O(m×n) |
| **Heap** | Top-k, priority queue | Kth Largest | O(n log k) | O(k) |
| **Intervals** | Merge, scheduling | Merge Intervals | O(n log n) | O(1) |
| **Trie** | Prefix matching, dictionary | Implement Trie | O(m) | O(m×α) |
| **Linked List** | Reversal, merging, cycles | LRU Cache | O(n) | O(1) |

## 🏢 Company Tags — Most Asked Patterns

| Company | Rounds | Top 3 Patterns | Must-Do Problems | Interview Style |
|---------|--------|---|---|---|
| **Google** | 3-4 | Graphs, DP, Binary Search, Trie | 200, 98, 76, 208 | System design + hard algos |
| **Amazon** | 3-4 | Arrays, BFS/DFS, DP, Heap | 1, 200, 198, 347 | Practical + scaling focus |
| **Meta** | 3-4 | Arrays, Trees, Graphs, Sliding Window | 1, 102, 200, 3 | Pattern matching, speed |
| **Apple** | 3 | Trees, Arrays, DP, Graphs | 226, 1, 62, 200 | Systems-aware solutions |
| **Microsoft** | 3-4 | Trees, Graphs, DP, Design | 98, 207, 322, 146 | Pragmatic, edge cases |
| **Nike** | 2-3 | Arrays, Trees, Graphs, DP | 238, 98, 200, 70 | Practical problem-solving |
| **Walmart** | 2-3 | Arrays, BFS/DFS, Sliding Window | 1, 200, 3, 15 | Speed + correctness |
| **Salesforce** | 2-3 | Trees, Graphs, DP, Heap | 226, 207, 322, 215 | Communication key |
| **Adobe** | 2-3 | Arrays, Trees, DP, Binary Search | 238, 100, 70, 75 | Creativity + optimization |

## 📚 Resources

### **Free**
- **[NeetCode.io](https://neetcode.io/)** — Video explanations for every problem, roadmap of 150 problems
- **[NeetCode 150](https://neetcode.io/practice)** — The curated list this course is based on
- **[Blind 75](https://blind.com/)** — Original must-do list (75 problems)
- **[LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)** — Pattern-based grouping
- **[Visualgo.net](https://visualgo.net/)** — Visualize data structures and algorithms
- **[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)** — Reference for complexities
- **[Python Collections Docs](https://docs.python.org/3/library/collections.html)** — Counter, defaultdict, deque

### **Mock Interviews**
- **[Pramp.com](https://www.pramp.com/)** — Free peer-to-peer mock interviews
- **[Interviewing.io](https://www.interviewing.io/)** — Mock interviews with real engineers

### **Paid (Worth It)**
- **[Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview)** — Pattern-based, comprehensive

## 🚀 How to Use This Repository

### **Setup**
```bash
git clone https://github.com/yourusername/leetcode-interview-prep.git
cd leetcode-interview-prep
```

### **Study Flow**
1. **Open the tracker**: Open `tracker/index.html` in your browser for a visual progress dashboard
2. **Read the pattern**: Start Week 1 with `problems/01-arrays-and-hashing/README.md`
3. **Solve the problem**: Open the `.py` file, understand both brute force and optimal solutions
4. **Implement yourself**: Type out the code from scratch 2-3 times
5. **Trace through examples**: Use the test cases; add your own edge cases
6. **Mark as solved**: Check the box in the tracker (auto-saves to localStorage)
7. **Mock interview**: Every Friday, do a timed run of 2-3 problems

### **Problem File Format**

Each `.py` file includes:
- **Docstring**: Problem statement, difficulty, pattern, companies
- **Two approaches**: Brute force + optimal with complexities
- **Interview script**: What to say during the interview
- **Working code**: Both solutions fully implemented
- **Test cases**: Minimum 4 tests that pass

Example:
```python
"""
Problem: Two Sum
LeetCode #: 1
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Pattern: HashMap
Companies: Amazon, Google, Microsoft, Meta, Apple

APPROACH:
Brute Force: O(n²)  |  Optimal: O(n) with HashMap
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []
```

## 🎬 Interview Framework — The 10-Step Method

**Total time: 45 minutes**

| Step | Time | What You Do | What Interviewer Evaluates |
|------|------|-------------|---------------------------|
| 1. **Clarify** | 0:00–1:00 | Ask about constraints, edge cases, examples | Communication, thoroughness |
| 2. **Examples** | 1:00–2:00 | Walk through one example; create edge case | Understanding |
| 3. **Brute Force** | 2:00–4:00 | State (don't code) the naive approach | Problem decomposition |
| 4. **Optimize** | 4:00–7:00 | Identify the pattern; suggest optimization | Pattern recognition |
| 5. **Plan** | 7:00–9:00 | Outline the algorithm; get a nod | Structured thinking |
| 6. **Code** | 9:00–30:00 | Write clean, talk while typing | Implementation, communication |
| 7. **Dry Run** | 30:00–35:00 | Trace through your example | Attention to detail |
| 8. **Edge Cases** | 35:00–38:00 | Test edge cases (empty, single, large) | Thoroughness |
| 9. **Complexity** | 38:00–40:00 | State time and space, justify | Analysis |
| 10. **Follow-up** | 40:00–45:00 | "What if X?" — be ready | Adaptability |

**Templates** → See `templates/interview-flow.md`

## 📊 Progress Tracker

Open [tracker/index.html](tracker/index.html) in your browser:
- ✅ Visual progress by week and pattern
- 📈 Heatmap of daily solving activity (GitHub-style)
- 📉 Pattern mastery radar chart
- 📋 Problem checklist with difficulty badges
- ⏰ Estimated completion date based on pace
- 🔥 Current streak counter

**How to update progress**: Click the checkbox next to each problem in the tracker. Progress automatically saves to `progress.json`.

## 📁 Repo Structure

```
leetcode-interview-prep/
├── tracker/
│   └── index.html                    # Visual progress dashboard
├── problems/
│   ├── 01-arrays-and-hashing/        # 6 problems
│   ├── 02-two-pointers/              # 4 problems
│   ├── 03-sliding-window/            # 4 problems
│   ├── 04-binary-search/             # 5 problems
│   ├── 05-stack/                     # 4 problems
│   ├── 06-linked-list/               # 5 problems
│   ├── 07-trees/                     # 9 problems
│   ├── 08-graphs/                    # 6 problems
│   ├── 09-backtracking/              # 3 problems
│   ├── 10-dynamic-programming/       # 8 problems
│   ├── 11-heap/                      # 3 problems
│   ├── 12-intervals/                 # 3 problems
│   └── 13-trie/                      # 2 problems
├── templates/
│   ├── interview-flow.md             # 10-step framework
│   ├── pattern-cheatsheet.md         # Patterns + templates
│   └── company-targets.md            # Company-specific prep
├── progress.json                      # Tracks solved problems
├── README.md                          # This file
└── .gitignore
```

## 💡 Study Tips

- **Code by hand first** — Don't rely on IDEs; practice writing on paper
- **Solve multiple ways** — Implement 2-3 approaches per problem
- **Explain out loud** — Use the interview scripts; get comfortable talking
- **Trace through examples** — Don't just run tests; manually trace key steps
- **Do mock interviews** — Use Pramp.com or Interviewing.io every week
- **Track patterns, not just problems** — After 2-3 problems, you recognize the pattern
- **Time yourself** — Easy should be <15min, Medium <30min, Hard <45min
- **Review frequently** — Revisit Week 1 problems every second week

## ⏱️ Estimated Timeline

- **Total time**: 40–50 hours of focused practice
- **Per week**: 5–6 hours (1 hour/day)
- **Break-in period**: Week 1-2 (get comfortable with patterns)
- **Ramp-up**: Week 3-7 (harder problems, faster pace)
- **Polish**: Week 8 (full mocks, review weak areas)

## 🎓 What You'll Learn

After completing this roadmap, you will:
- ✅ Recognize 13 core coding patterns instantly
- ✅ Know the time/space complexities by heart
- ✅ Solve medium-difficulty problems in <30 minutes
- ✅ Handle hard problems with confidence
- ✅ Communicate clearly during interviews
- ✅ Optimize solutions on the fly
- ✅ Ace MAANG + mid-level interviews

## 🤝 Contributing

Found a bug? Better solution? Typo in explanation? Open an issue or PR!

## 📝 License

This repository is open source and available under the MIT License.

---

**Ready?** Start with [problems/01-arrays-and-hashing/README.md](problems/01-arrays-and-hashing/README.md) and open [tracker/index.html](tracker/index.html) now!

**Questions?** Review [templates/interview-flow.md](templates/interview-flow.md) for the complete 10-step interview framework.

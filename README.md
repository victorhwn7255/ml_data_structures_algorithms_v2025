<div align="center">

![NTU Banner](./assets/ntu_banner.png)

<br>

# AI/ML Interview Prep Arsenal

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Data_Structures-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white" alt="Data Structures" />
  <img src="https://img.shields.io/badge/Algorithms-4ECDC4?style=for-the-badge&logo=algolia&logoColor=white" alt="Algorithms" />
  <img src="https://img.shields.io/badge/Machine_Learning-FF9F43?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI/ML" />
</p>

<p align="center">
  <strong>🎯 Master the fundamentals. Ace the interview. Land the dream job.</strong>
</p>

<p align="center">
  <em>A comprehensive collection of Data Structures & Algorithms practice problems specifically curated for AI/ML engineers and data scientists.</em>
</p>

---

</div>


```python
class InterviewPrep:
    def __init__(self):
        self.focus = "AI/ML Engineers"
        self.approach = "Practical + Visual"
        self.goal = "Interview Success"
    
    def get_features(self):
        return [
            "🔍 Clean, readable Python implementations",
            "🎨 Beautiful tree visualizations", 
            "📝 Detailed explanations for each solution",
            "🧪 Comprehensive test cases",
            "📊 Time & space complexity analysis",
            "🔄 Multiple solution approaches"
        ]
```
<br>

## 📚 Problem Categories

<div align="center">

### 🎯 **Core Data Structures & Algorithms**

</div>

<details>
<summary><strong>🌳 Trees & Graphs</strong> - <em>Master hierarchical data & graph traversals</em></summary>

```
🔹 Depth-First Search (DFS)   🔹 Binary Tree Traversals
🔹 Breadth-First Search (BFS) 🔹 Tree Visualization Tools  
🔹 Graph DFS & BFS           🔹 Connected Components
🔹 Lowest Common Ancestor    🔹 Path Finding & Cycle Detection
```
</details>

<details>
<summary><strong>🔗 Linked Lists & Pointers</strong> - <em>Navigate linear data structures efficiently</em></summary>

```
🔹 Two Pointer Techniques    🔹 Fast & Slow Pointers
🔹 List Reversal & Merging   🔹 Cycle Detection (Floyd's)
🔹 Middle Element Finding    🔹 Palindrome Detection
🔹 Odd-Even List Reordering  🔹 Node Deletion Patterns
```
</details>

<details>
<summary><strong>🪟 Sliding Window & Arrays</strong> - <em>Optimize subarray & substring problems</em></summary>

```
🔹 Fixed Window Algorithms    🔹 Variable Window Techniques
🔹 Maximum Subarray Problems  🔹 Substring Pattern Matching
🔹 Longest Subarray Variants  🔹 String Vowel Optimization
🔹 Consecutive Elements       🔹 Window Size Optimization
```
</details>

<details>
<summary><strong>🗂️ Hash Maps & Sets</strong> - <em>Master O(1) lookups & frequency problems</em></summary>

```
🔹 Frequency Counting         🔹 Unique Occurrence Detection
🔹 Array Difference Finding   🔹 String Anagram Problems
🔹 Row-Column Pair Matching   🔹 Majority Element Finding
🔹 Set Operations            🔹 Close String Validation
```
</details>

<details>
<summary><strong>🔙 Backtracking & Recursion</strong> - <em>Systematic exploration & recursive patterns</em></summary>

```
🔹 Combination Sum Problems   🔹 Letter Combinations
🔹 Recursive Tree Operations  🔹 Factorial Calculations
🔹 Divide & Conquer          🔹 Solution Space Exploration
🔹 Base Case Design          🔹 State Backtracking
```
</details>

<details>
<summary><strong>🔍 Binary Search & Sorting</strong> - <em>Efficient searching & ordering algorithms</em></summary>

```
🔹 BST Search & Operations    🔹 Peak Element Finding
🔹 Optimization Problems      🔹 Guess Number Games
🔹 Spell-Potion Pairing      🔹 Eating Speed Optimization
🔹 Bubble, Selection, Insert  🔹 Comparison-based Sorting
```
</details>

<details>
<summary><strong>🧮 Dynamic Programming</strong> - <em>Optimization through memoization & bottom-up approaches</em></summary>

```
🔹 Fibonacci Sequences        🔹 Tribonacci Variations
🔹 House Robber Problems      🔹 Climbing Stairs Optimization
🔹 Domino & Tromino Tiling    🔹 2D Matrix Problems
🔹 Stock Trading Strategies   🔹 String Edit Distance
🔹 Longest Common Subsequence 🔹 Unique Path Counting
```
</details>

<details>
<summary><strong>🏆 Advanced Data Structures</strong> - <em>Heaps, stacks, queues & specialized structures</em></summary>

```
🔹 Priority Queue (Heap)      🔹 Monotonic Stack Problems
🔹 Stack-based Parsing        🔹 Queue Simulations
🔹 Trie (Prefix Tree)         🔹 Interval Scheduling
🔹 Bit Manipulation          🔹 Mathematical Optimizations
```
</details>
<br>

## 🏗️ Repository Structure

```
ml_interview_prep/
├── 🌳 algorithms/
│   ├── 🔙 backtracking/           # Combination sum, letter combinations
│   ├── 🔍 binary_search/          # BST operations, peak finding, optimization
│   ├── 🔢 bit_manipulation/       # Counting bits, XOR operations  
│   ├── 🌊 breadth_first_search/   # Level-order tree traversal, BFS
│   ├── 🔍 depth_first_search/     # Tree DFS, path finding, recursion
│   ├── 🔄 dynamic_programming/    # DP classics: fibonacci, house robber
│   ├── 🏃 fast_and_slow/          # Two pointer techniques, cycle detection
│   ├── 🌐 graph_bfs/              # Graph traversal, shortest paths
│   ├── 🌐 graph_dfs/              # Connected components, graph exploration
│   ├── 🗂️ hash_map/               # Frequency counting, lookup optimizations
│   ├── ⏱️ intervals/               # Interval merging, scheduling problems
│   ├── 🔗 linked_list/            # List manipulation, reversal, cycles
│   ├── 📊 monotonic_stack/        # Stack-based optimization problems
│   ├── 📈 multi_dimensional/      # 2D DP, matrix problems, stock trading
│   ├── ➕ prefix_sum/             # Cumulative sums, range queries
│   ├── 🏆 priority_queue/         # Heap operations, top-K problems
│   ├── 🔄 queue/                  # FIFO operations, BFS implementations
│   ├── 🔄 recursion/              # Recursive patterns, divide & conquer
│   ├── 🪟 sliding_window/         # Subarray optimization, string patterns
│   ├── 📊 sorting/                # Fundamental sorting algorithms
│   ├── 📚 stack/                  # LIFO operations, parentheses matching
│   ├── 🌲 trie/                   # Prefix trees, autocomplete systems
│   └── 👥 two_pointers/           # Array manipulation, palindromes
├── 🏛️ data_structures/
│   ├── binary_search_tree.py
│   ├── linked_list.py
│   ├── doubly_linked_list.py
│   ├── hash_table.py
│   ├── heap.py
│   ├── pointers.py
│   ├── queue.py
│   ├── stack.py
│   └── graph.py
├── 🛠️ utils/
│   └── tree_utils.py  # Beautiful tree visualization
└── 📋 README.md
```
<br>

## 🎯 Featured Solutions

### 🌟 Tree Visualization
Our custom tree visualization tool makes debugging and understanding tree problems a breeze:

```python
tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.print_tree()  # Beautiful ASCII art output!
```

### 🔥 Optimized Implementations
Each solution includes:
- ⚡ **Time Complexity**: Big O analysis
- 💾 **Space Complexity**: Memory usage breakdown  
- 🎨 **Multiple Approaches**: Iterative vs Recursive
- 🧪 **Test Cases**: Edge cases covered
<br>

## 🤝 Contributing

Found a bug? Have a better solution? Want to add more problems?

1. 🍴 Fork the repository
2. 🔧 Create your feature branch (`git checkout -b feature/amazing-solution`)
3. 💾 Commit your changes (`git commit -m 'Add amazing solution'`)
4. 📤 Push to the branch (`git push origin feature/amazing-solution`)
5. 🎉 Open a Pull Request
<br>

## 📈 Progress Tracking

**📊 Total: 90+ algorithm implementations across 20+ categories**

### Core Fundamentals ✅
- [x] **Trees & Graphs**: 13+ problems (DFS, BFS, graph traversal)
- [x] **Linked Lists**: 6+ problems (reversal, cycles, two pointers)
- [x] **Hash Maps**: 5+ problems (frequency, lookups, anagrams)
- [x] **Two Pointers**: 9+ problems (palindromes, merging, duplicates)

### Advanced Topics ✅
- [x] **Dynamic Programming**: 9+ problems (fibonacci, house robber, 2D DP)
- [x] **Binary Search**: 6+ problems (BST operations, optimization)
- [x] **Sliding Window**: 4+ problems (subarray optimization)
- [x] **Backtracking**: 3+ problems (combination sum, letter combos)

### Specialized Structures ✅
- [x] **Priority Queue/Heap**: 4+ problems (top-K, scheduling)
- [x] **Stack & Queue**: 7+ problems (monotonic stack, parsing)
- [x] **Trie**: 2+ problems (prefix trees, autocomplete)
- [x] **Bit Manipulation**: 3+ problems (XOR, counting bits)

### Problem-Solving Patterns ✅
- [x] **Prefix Sum**: 3+ problems (range queries, cumulative sums)
- [x] **Intervals**: 2+ problems (scheduling, merging)
- [x] **Sorting Algorithms**: 3+ fundamental sorts
- [x] **Fast & Slow Pointers**: 2+ problems (cycle detection)
- [x] **Graph Algorithms**: 7+ problems (DFS/BFS variations)
- [x] **Recursion**: 2+ problems (divide & conquer patterns)

### Mathematical & Multi-dimensional ✅
- [x] **Multi-dimensional DP**: 4+ problems (matrix, stock trading)
- [x] **Monotonic Stack**: 2+ problems (temperature, stock span)


---

<div align="center">

<p>
  <strong>Happy Coding! 🚀</strong>
</p>

<p align="center">
  <sub>
    <strong>Created and managed by <a href="https://www.linkedin.com/in/vic-hee-17a86b378/" style="text-decoration: none; color: #0366d6;">Vic</a></strong><br>
    <em>In collaboration with NTU LeetCode Club (CCDS)</em>
  </sub>
</p>

</div>

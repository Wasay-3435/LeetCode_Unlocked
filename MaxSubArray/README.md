
# 53. Maximum Subarray

**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Greedy, Kadane's Algorithm

## Problem

Given an integer array `nums`, find the contiguous
subarray with the largest sum and return that sum.

A subarray must contain at least one element.

### Example

**Input:**
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:**
```python
6
```

**Explanation:**

The maximum-sum subarray is `[4, -1, 2, 1]`.

Its sum is `4 + (-1) + 2 + 1 = 6`.

---

## Approach 1: Brute Force

### Intuition

Generate every possible contiguous subarray, calculate
its sum, and keep track of the maximum sum.

### Algorithm

1. Initialize `max_sum` to negative infinity.
2. Select each starting index using the outer loop.
3. Initialize `current_sum = 0`.
4. Extend the subarray using the inner loop.
5. Add each new element to `current_sum`.
6. Update `max_sum` whenever a larger sum is found.
7. Return `max_sum`.

### Complexity

- **Time:** O(n²) — two nested loops.
- **Auxiliary space:** O(1) — only a few variables.

---

## Approach 2: Kadane's Algorithm

### Intuition

At every element, decide whether to:

- Extend the previous subarray.
- Start a new subarray from the current element.

Choose whichever produces the larger sum.

### Algorithm

1. Initialize `current_sum` and `max_sum` with the first element.
2. Traverse the array starting from index 1.
3. Calculate the maximum between:
   - The current element.
   - The previous subarray sum plus the current element.
4. Update `max_sum` if `current_sum` is larger.
5. Return `max_sum`.

### Dry Run

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| Index | Number | Current Sum | Maximum Sum |
|---:|---:|---:|---:|
| 0 | -2 | -2 | -2 |
| 1 | 1 | 1 | 1 |
| 2 | -3 | -2 | 1 |
| 3 | 4 | 4 | 4 |
| 4 | -1 | 3 | 4 |
| 5 | 2 | 5 | 5 |
| 6 | 1 | 6 | 6 |
| 7 | -5 | 1 | 6 |
| 8 | 4 | 5 | 6 |

**Final answer: 6**

### Complexity

- **Time:** O(n) — one traversal of the array.
- **Auxiliary space:** O(1) — only two variables are maintained.

---

## Complexity Comparison

| Metric | Brute Force | Kadane's Algorithm |
|---|---|---|
| Time | O(n²) | O(n) |
| Auxiliary space | O(1) | O(1) |
| Approach | Generate subarrays | Extend or restart |

## Key Learnings

- A subarray must contain contiguous elements.
- Negative numbers are valid elements.
- The maximum subarray can contain just one element.
- Kadane's Algorithm decides whether to extend or restart.
- Initialize with the first element, not zero, to handle
  arrays containing only negative numbers.
- Kadane's Algorithm reduces time complexity from O(n²)
  to O(n).

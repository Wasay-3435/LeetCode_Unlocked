
# 152. Maximum Product Subarray

**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming

## Problem

Given an integer array `nums`, find a contiguous subarray
that has the largest product and return that product.

A subarray must contain at least one element.

### Example 1

**Input:**
```python
nums = [2, 3, -2, 4]
```

**Output:**
```python
6
```

**Explanation:** The subarray `[2, 3]` has the maximum
product: `2 * 3 = 6`.

### Example 2

**Input:**
```python
nums = [-2, 0, -1]
```

**Output:**
```python
0
```

---

## Approach 1: Brute Force

### Intuition

Generate every possible contiguous subarray, calculate
its product, and keep track of the maximum product.

### Algorithm

1. Initialize `max_product` to negative infinity.
2. Choose each starting index using the outer loop.
3. Initialize `current_product = 1`.
4. Extend the subarray using the inner loop.
5. Multiply the current product by the next element.
6. Update the maximum product.
7. Return the result.

### Complexity

- **Time:** O(n²) — two nested loops.
- **Auxiliary space:** O(1) — only a few variables.

---

## Approach 2: Dynamic Programming (Optimized)

### Intuition

Negative numbers make this problem interesting.

Multiplying two negative numbers produces a positive
number. Therefore, the minimum product can become the
maximum product when multiplied by another negative.

We maintain three variables:

- `max_product`: Maximum product ending at the current index.
- `min_product`: Minimum product ending at the current index.
- `result`: Maximum product found across the entire array.

### Algorithm

1. Initialize all three variables with the first element.
2. Traverse the array starting from index 1.
3. For each number, calculate three candidates:
   - The current number itself.
   - Previous maximum product multiplied by current number.
   - Previous minimum product multiplied by current number.
4. Update `max_product` using the largest candidate.
5. Update `min_product` using the smallest candidate.
6. Update the overall result.
7. Return the result.

### Dry Run

Input: `[-2, 3, -4]`

| Index | Number | Maximum product | Minimum product | Result |
|---:|---:|---:|---:|---:|
| 0 | -2 | -2 | -2 | -2 |
| 1 | 3 | 3 | -6 | 3 |
| 2 | -4 | 24 | -12 | 24 |

**Final answer: 24**

### Complexity

- **Time:** O(n) — one traversal of the array.
- **Auxiliary space:** O(1) — only a constant number
  of variables are maintained.

---

## Complexity Comparison

| Metric | Brute Force | Optimized DP |
|---|---|---|
| Time | O(n²) | O(n) |
| Auxiliary space | O(1) | O(1) |
| Technique | Generate subarrays | Track maximum and minimum products |

## Key Learnings

- A subarray must contain contiguous elements.
- Negative numbers can change the maximum and minimum.
- Two negative numbers produce a positive product.
- Track both maximum and minimum products.
- Zero is handled naturally by the algorithm.
- The optimized solution runs in O(n) time.

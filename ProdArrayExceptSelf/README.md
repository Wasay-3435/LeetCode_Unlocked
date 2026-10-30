
# 238. Product of Array Except Self

**Difficulty:** Medium  
**Topics:** Array, Prefix Product, Suffix Product

## Problem

Given an integer array `nums`, return an array `answer`
where `answer[i]` is the product of all elements in
`nums` except `nums[i]`.

The solution must not use division and should run in O(n)
time.

### Example

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
[24, 12, 8, 6]
```

---

## Approach 1: Brute Force

### Intuition

For every element, multiply all other elements while
skipping the current index.

### Algorithm

1. Create an empty answer list.
2. Iterate through every index.
3. Initialize product to 1.
4. Iterate through the array again.
5. Skip the current index and multiply the remaining values.
6. Append the product to the answer list.

### Complexity

- **Time:** O(n²) — nested loops.
- **Auxiliary space:** O(1), excluding the output array.
- **Output space:** O(n).

---

## Approach 2: Prefix and Suffix Products

### Intuition

The product of all elements except the current element
can be divided into two parts:

- Prefix: Product of all elements to the left.
- Suffix: Product of all elements to the right.

Therefore:

`answer[i] = prefix[i] * suffix[i]`

### Algorithm

**First pass — Prefix:**

1. Initialize `answer` with 1s.
2. Initialize `prefix = 1`.
3. Traverse from left to right.
4. Store the current prefix in `answer[i]`.
5. Multiply prefix by the current number.

**Second pass — Suffix:**

1. Initialize `suffix = 1`.
2. Traverse from right to left.
3. Multiply `answer[i]` by suffix.
4. Multiply suffix by the current number.

### Dry Run

Input: `[1, 2, 3, 4]`

After the prefix pass:

`answer = [1, 1, 2, 6]`

After the suffix pass:

`answer = [24, 12, 8, 6]`

### Complexity

- **Time:** O(n) — two passes through the array.
- **Auxiliary space:** O(1), excluding the output array.
- **Output space:** O(n).

---

## Complexity Comparison

| Metric | Brute Force | Optimized |
|---|---|---|
| Time | O(n²) | O(n) |
| Auxiliary space | O(1) | O(1) |
| Output space | O(n) | O(n) |
| Division | No | No |

## Key Learnings

- Prefix means product of elements to the left.
- Suffix means product of elements to the right.
- 1 is the multiplicative identity.
- Two passes allow us to calculate the result efficiently.
- Processing from right to left builds the suffix product.
- The optimized solution handles zeros without special cases.

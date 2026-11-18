
# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium

**Topics:** Array, Binary Search

## Problem Description

Given an array of unique integers that was originally sorted in ascending order but then rotated at an unknown pivot, return the minimum element.

The algorithm must run in O(log n) time.

### Example 1

**Input:**
```python
nums = [3, 4, 5, 1, 2]
```

**Output:**
```python
1
```

### Example 2

**Input:**
```python
nums = [4, 5, 6, 7, 0, 1, 2]
```

**Output:**
```python
0
```

### Example 3

**Input:**
```python
nums = [11, 13, 15, 17]
```

**Output:**
```python
11
```

---

## Approach 1: Brute Force

### Intuition

Check every element in the array and keep track of the smallest value.

### Algorithm

1. Initialize `minimum` with the first element.
2. Iterate through the entire array.
3. Compare each element with the current minimum.
4. Update the minimum whenever a smaller element is found.
5. Return the minimum.

### Code

```python
def find_min_brute_force(nums: list[int]) -> int:
    minimum = nums[0]

    for num in nums:
        minimum = min(minimum, num)

    return minimum
```

### Complexity Analysis

- **Time Complexity:** O(n) — every element is visited once.
- **Auxiliary Space Complexity:** O(1) — only one variable is used.

---

## Approach 2: Binary Search (Optimized)

### Intuition

A rotated sorted array consists of two sorted portions.

The minimum element is located at the rotation point.

Instead of checking every element, binary search repeatedly eliminates approximately half of the search range.

We compare the middle element with the rightmost element to determine which portion may contain the minimum.

### Algorithm

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. Continue while `left < right`.
3. Calculate the middle index.
4. Compare `nums[mid]` with `nums[right]`.
5. If `nums[mid] > nums[right]`, the minimum must be to the right of `mid`. Set `left = mid + 1`.
6. Otherwise, the minimum is at `mid` or to its left. Set `right = mid`.
7. When both pointers meet, return `nums[left]`.

### Code

```python
def find_min(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
```

### Dry Run

**Input:**
```python
nums = [4, 5, 6, 7, 0, 1, 2]
```

Initial values:

```python
left = 0
right = 6
```

| Iteration | left | right | mid | nums[mid] | nums[right] | Decision |
|---|---:|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 7 | 2 | left = mid + 1 = 4 |
| 2 | 4 | 6 | 5 | 1 | 2 | right = mid = 5 |
| 3 | 4 | 5 | 4 | 0 | 1 | right = mid = 4 |

Now:

```python
left = 4
right = 4
```

The loop stops because `left < right` is false.

Return:

```python
nums[4]  # 0
```

**Output:** `0`

### Understanding the Conditions

**Case 1: `nums[mid] > nums[right]`**

The minimum is strictly to the right of `mid`.

```python
left = mid + 1
```

**Case 2: `nums[mid] <= nums[right]`**

The minimum is at `mid` or somewhere to its left.

```python
right = mid
```

We keep `mid` because it could itself be the minimum.

### Complexity Analysis

- **Time Complexity:** O(log n) — the search range is approximately halved in each iteration.
- **Auxiliary Space Complexity:** O(1) — only a constant number of variables are used.

---

## Complexity Comparison

| Metric | Brute Force | Binary Search |
|---|---|---|
| Time Complexity | O(n) | O(log n) |
| Auxiliary Space | O(1) | O(1) |
| Strategy | Linear Search | Binary Search |

## Key Takeaways

- A rotated sorted array contains two sorted portions.
- The minimum is located at the rotation point.
- Comparing `nums[mid]` with `nums[right]` helps identify which half contains the minimum.
- Use `left = mid + 1` when `nums[mid] > nums[right]`.
- Use `right = mid` otherwise, because `mid` could be the answer.
- The optimized solution achieves O(log n) time complexity.

**Important:** This solution assumes unique elements, as specified in LeetCode #153.

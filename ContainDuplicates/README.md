
# 217. Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Set

## Problem

Given an integer array `nums`, return `True` if any value
appears at least twice. Return `False` if every element
is distinct.

## Examples

| Input | Output |
|---|---|
| `[1, 2, 3, 1]` | `True` |
| `[1, 2, 3, 4]` | `False` |
| `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` | `True` |

---

## Approach 1: Brute Force

### Intuition

Compare every element with all the elements after it.
If any pair matches, a duplicate exists.

### Algorithm

1. Select an element using the outer loop.
2. Compare it with every later element using the inner loop.
3. Return `True` if a matching pair is found.
4. If no pair matches, return `False`.

### Complexity

- **Time:** `O(n^2)` worst case.
- **Auxiliary space:** `O(1)`.

The nested loops perform many comparisons, but they do not
create an additional collection of pairs.

---

## Approach 2: Hash Set

### Intuition

Maintain a set containing values already encountered.

If the current value is already in the set, return `True`.
Otherwise, add it and continue.

### Algorithm

1. Create an empty set called `seen`.
2. Visit each number in the array.
3. If the number is in `seen`, return `True`.
4. Otherwise, add the number to `seen`.
5. Return `False` if the loop finishes.

### Complexity

- **Time:** `O(n)` average.
- **Auxiliary space:** `O(n)` worst case.

Each number is processed once. The set may store all `n`
numbers when no duplicates exist.

---

## Complexity Comparison

| Metric | Brute Force | Hash Set |
|---|---|---|
| Time | `O(n^2)` | `O(n)` average |
| Auxiliary space | `O(1)` | `O(n)` |
| Technique | Compare pairs | Remember seen values |

## Key Learnings

- A Python set stores unique values.
- Set membership checks are `O(1)` on average.
- Nested loops do not necessarily imply `O(n^2)` space.
- A single loop can still use `O(n)` space if it builds
  a collection that grows with the input.
- The hash-set approach trades additional memory for
  faster execution.

## Run the Solutions

Run both implementations and the built-in example checks:

```bash
python solution.py
```

The script checks five inputs against their expected
outputs using Python assertions.

## LeetCode Submission

Submit the `Solution` class and its `containsDuplicate`
method from `solution.py`.

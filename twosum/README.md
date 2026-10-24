
# Two Sum

- **LeetCode:** [Problem #1](https://leetcode.com/problems/two-sum/)
- **Difficulty:** Easy
- **Topics:** Array, Hash Table
- **Language:** Python

## Problem

Given an array of integers `nums` and an integer `target`,
return the indices of two distinct elements whose sum equals
the target.

Assume exactly one valid answer exists. The same element
cannot be used twice.

## Examples

### Example 1

Input:
- `nums = [2, 7, 11, 15]`
- `target = 9`

Output: `[0, 1]`

Explanation: `nums[0] + nums[1] = 2 + 7 = 9`.

### Example 2

Input:
- `nums = [3, 2, 4]`
- `target = 6`

Output: `[1, 2]`

Explanation: `nums[1] + nums[2] = 2 + 4 = 6`.

### Example 3

Input:
- `nums = [3, 3]`
- `target = 6`

Output: `[0, 1]`

Explanation: The two distinct elements both have value 3.

## Approach 1: Brute Force

Check every possible pair using nested loops.

For each index `i`, examine the elements after it.
If `nums[i] + nums[j] == target`, return `[i, j]`.

### Complexity

- Time: O(n²)
- Auxiliary space: O(1)

## Approach 2: Hash Map (Optimized)

Maintain a dictionary called `seen`, storing each previously
visited number as a key and its index as the value.

For each number:

1. Calculate `complement = target - num`.
2. Check whether the complement exists in `seen`.
3. If it exists, return the stored index and the current index.
4. Otherwise, store the current number and its index.

### Why it works

If `num + complement = target`, finding the complement
among previously visited numbers gives us a valid pair.

We check before inserting the current number so that an
element cannot be paired with itself.

### Complexity

- Time: O(n) average
- Auxiliary space: O(n) worst case

Here, `n` is the number of elements in the input array.
Hash-map lookup and insertion are O(1) on average.

## Key Learnings

- Array indices start at zero in Python.
- The problem asks for indices, not values.
- A complement is `target - current_number`.
- A hash map avoids repeatedly searching for pairs.
- The optimized approach trades extra memory for faster execution.
- Always consider edge cases, including duplicate values.

## Test Cases

- `[2, 7, 11, 15]`, target `9` -> `[0, 1]`
- `[3, 2, 4]`, target `6` -> `[1, 2]`
- `[3, 3]`, target `6` -> `[0, 1]`

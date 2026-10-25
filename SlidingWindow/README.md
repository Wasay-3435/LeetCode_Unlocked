
# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Topics:** Array, Greedy, Sliding Window (study category)

## Problem

Given an array `prices`, where `prices[i]` represents
the stock price on day `i`, choose one day to buy and a
later day to sell.

Return the maximum possible profit. If no profitable
transaction is possible, return `0`.

You must buy before you sell.

### Example

**Input**
```python
prices = [7, 1, 5, 3, 6, 4]
```

**Output**
```text
5
```

**Explanation:** Buy at price `1` and sell later at price
`6`. The profit is `6 - 1 = 5`.

---

## Approach 1: Brute Force

### Intuition

Try every valid pair of buying and selling days. Calculate
the profit for each pair and keep the largest profit.

### Algorithm

1. Initialize `max_profit = 0`.
2. Choose each day as the buying day.
3. Examine every later day as the selling day.
4. Calculate `selling price - buying price`.
5. Update the maximum profit.
6. Return the result.

### Complexity

- **Time:** `O(n^2)` — checks every valid pair of days.
- **Auxiliary space:** `O(1)` — uses a constant number of variables.

---

## Approach 2: Optimized One-Pass Greedy

### Intuition

For each selling day, the best buying day is the earlier day
with the lowest price.

Instead of repeatedly searching for that price, maintain
the minimum price seen so far.

### Algorithm

1. Initialize `min_price` to infinity.
2. Initialize `max_profit = 0`.
3. Visit each price once.
4. Update `min_price` if the current price is lower.
5. Calculate `current price - min_price`.
6. Update `max_profit` if the calculated profit is higher.
7. Return `max_profit`.

### Dry Run

Input: `[7, 1, 5, 3, 6, 4]`

| Day | Price | Minimum price | Current profit | Best profit |
|---:|---:|---:|---:|---:|
| 0 | 7 | 7 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 5 | 1 | 4 | 4 |
| 3 | 3 | 1 | 2 | 4 |
| 4 | 6 | 1 | 5 | 5 |
| 5 | 4 | 1 | 3 | 5 |

**Result:** `5`

### Why It Works

For each day, the minimum price seen so far gives the
cheapest available buying opportunity up to that day.
Subtracting it from the current price gives the best profit
for that selling day. Keeping the maximum of these profits
therefore finds the global maximum.

### Complexity

- **Time:** `O(n)` — visits each price once.
- **Auxiliary space:** `O(1)` — stores only a few variables.

---

## Complexity Comparison

| Metric | Brute Force | Optimized |
|---|---|---|
| Time | `O(n^2)` | `O(n)` |
| Auxiliary space | `O(1)` | `O(1)` |
| Strategy | Check all pairs | Track minimum and best profit |

---

## Key Takeaways

- Buying must happen before selling.
- Start the maximum profit at zero.
- Remember the lowest price encountered so far.
- Evaluate the profit at each selling opportunity.
- The optimized solution reduces time complexity from
  `O(n^2)` to `O(n)`.

## LeetCode Submission

Submit the `Solution` class and its `maxProfit` method
from `solution.py`.

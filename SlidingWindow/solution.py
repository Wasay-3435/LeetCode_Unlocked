
def max_profit_brute_force(prices: list[int]) -> int:
    """Return the maximum profit by checking every valid buy/sell pair."""
    max_profit = 0

    for buy_day in range(len(prices)):
        for sell_day in range(buy_day + 1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit)

    return max_profit


def max_profit(prices: list[int]) -> int:
    """Return the maximum profit in one pass using the minimum price so far."""
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


class Solution:
    """LeetCode-compatible solution."""

    def maxProfit(self, prices: list[int]) -> int:
        return max_profit(prices)


if __name__ == "__main__":
    example = [7, 1, 5, 3, 6, 4]

    print("Brute force:", max_profit_brute_force(example))
    print("Optimized:", max_profit(example))

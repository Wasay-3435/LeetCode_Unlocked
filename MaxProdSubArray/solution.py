
# Approach 1: Brute Force
def max_product_brute_force(nums: list[int]) -> int:
    max_product = float("-inf")

    for i in range(len(nums)):
        current_product = 1

        for j in range(i, len(nums)):
            current_product *= nums[j]
            max_product = max(max_product, current_product)

    return max_product


# Approach 2: Dynamic Programming (Optimized)
def max_product(nums: list[int]) -> int:
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        candidates = (
            num,
            max_product * num,
            min_product * num
        )

        max_product = max(candidates)
        min_product = min(candidates)

        result = max(result, max_product)

    return result

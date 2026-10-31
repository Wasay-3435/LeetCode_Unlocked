
# Approach 1: Brute Force
def max_subarray_brute_force(nums: list[int]) -> int:
    max_sum = float("-inf")

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


# Approach 2: Kadane's Algorithm (Optimized)
def max_subarray(nums: list[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

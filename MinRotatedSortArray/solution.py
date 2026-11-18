
# Approach 1: Brute Force
def find_min_brute_force(nums: list[int]) -> int:
    minimum = nums[0]

    for num in nums:
        minimum = min(minimum, num)

    return minimum


# Approach 2: Binary Search (Optimized)
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


# Approach 1: Brute Force
def contains_duplicate_brute_force(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# Approach 2: Hash Set (Optimized)
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


"""
Problem: Two Sum
LeetCode #1
Difficulty: Easy
Topic: Array, Hash Table
"""


def two_sum_brute_force(nums, target):
    """Check every pair of distinct elements."""
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find the answer using a hash map."""
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []  


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Output:", result)

    # Basic test cases
    assert result == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]

    # Compare with brute force
    assert two_sum_brute_force(nums, target) == result

    print("All tests passed!")

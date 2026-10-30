
# Approach 1: Brute Force
def product_except_self_brute_force(nums: list[int]) -> list[int]:
    answer = []

    for i in range(len(nums)):
        product = 1

        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        answer.append(product)

    return answer


# Approach 2: Prefix and Suffix Products (Optimized)
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1

    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

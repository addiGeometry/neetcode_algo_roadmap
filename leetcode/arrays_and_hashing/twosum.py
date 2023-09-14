def two_sum(nums: list[int], target: int) -> list[int]:
    numbers = {}
    for i, num in enumerate(nums):
        to_find = target - num
        if to_find in numbers:
            return sorted([i, numbers[to_find]])
        numbers[num] = i
from typing import List


# brute force for fun, beats 26%, lol!
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# O(n) time and space
def twoSum2(nums: List[int], target: int) -> List[int]:
    diffs = {}
    for i, num in enumerate(nums):
        if num in diffs:
            return [diffs[num], i]

        diffs[target - num] = i
    return []


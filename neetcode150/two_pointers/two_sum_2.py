from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while (temp_sum := numbers[l] + numbers[r]) != target:
        if temp_sum > target:
            r -= 1
        else:
            l += 1

    return [l + 1, r + 1]

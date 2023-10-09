from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


def containsDuplicate2(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

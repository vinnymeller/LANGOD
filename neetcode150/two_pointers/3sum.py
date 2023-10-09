from typing import List


# made a lot of oopsies on this one definitely must review
def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums.sort()

    if nums[0] > 0:
        return []

    solutions = []
    for i, num in enumerate(nums[:-2]):
        if num > 0:
            return solutions

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_sum = num + nums[l] + nums[r]

            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                solutions.append([num, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return solutions

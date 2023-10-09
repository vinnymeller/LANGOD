import operator
from functools import reduce
from itertools import accumulate
from typing import List


def trap(height: List[int]) -> int:
    left_to_right: List[int] = list(accumulate(height, max))
    right_to_left: List[int] = list(accumulate(height[::-1], max))
    right_to_left.reverse()

    total = 0

    for i in range(len(height)):
        lh = left_to_right[i]
        rh = right_to_left[i]
        min_height = lh if lh < rh else rh

        diff = max(0, min_height - height[i])

        total += diff
    return total


# Improvement from looking at solution:
# Don't have to pre-compute max to left and right, it can be done as I move the pointers
# Original is still O(n) but it runs through the list multiple times instead of once
def trap2(height: List[int]) -> int:
    total = 0

    l = 0
    r = len(height) - 1
    lm = height[l]
    rm = height[r]

    while l < r:
        if lm < rm:
            l += 1
            lm = max(lm, height[l])
            total += lm - height[l]
        else:
            r -= 1
            rm = max(rm, height[r])
            total += rm - height[r]
    return total

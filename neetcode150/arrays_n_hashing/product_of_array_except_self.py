import operator
from collections import deque
from itertools import accumulate
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    left_to_right = deque(accumulate(nums, operator.mul))
    left_to_right.pop()
    left_to_right.appendleft(1)
    right_to_left = list(accumulate(reversed(nums), operator.mul))[:-1][::-1]
    right_to_left.append(1)

    return [l * r for l, r in zip(left_to_right, right_to_left)]

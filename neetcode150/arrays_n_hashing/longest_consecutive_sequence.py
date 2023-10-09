from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    unique_nums = {num: False for num in nums}

    longest_consecutive = 1

    for num in unique_nums.keys():
        if unique_nums[num]:
            continue

        unique_nums[num] = True
        consecutive = 1

        # check consecutive nums below
        below_num = num - 1
        while below_num in unique_nums:
            unique_nums[below_num] = True
            consecutive += 1
            below_num -= 1

        above_num = num + 1
        while above_num in unique_nums:
            unique_nums[above_num] = True
            consecutive += 1
            above_num += 1

        longest_consecutive = max(longest_consecutive, consecutive)

    return longest_consecutive



# improvement from looking at solution:
# instead of checking above and below and then marking whether the num has been visited
# always make sure we're starting at the beginning of a sequence by checking that (num-1) not in the set, and then searching forward
# no extra memory and probably faster
def longestConsecutive2(nums: List[int]) -> int:
    if not nums:
        return 0

    unique_nums = set(nums)

    longest = 1
    for num in unique_nums:
        if (num - 1) in unique_nums:
            continue

        length = 1
        while num + length in unique_nums:
            length += 1

        longest = max(longest, length)

    return longest

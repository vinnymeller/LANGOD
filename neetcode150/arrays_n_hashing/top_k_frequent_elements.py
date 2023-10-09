from collections import defaultdict, deque
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    pairs = [(num, value) for num, value in counts.items()]

    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    return [pair[0] for pair in pairs[:k]]

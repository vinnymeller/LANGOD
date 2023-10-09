from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in strs:
        letter_order = tuple(sorted([c for c in word]))
        groups[letter_order].append(word)

    return list(groups.values())
    

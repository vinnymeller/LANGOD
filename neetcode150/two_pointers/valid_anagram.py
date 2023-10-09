from collections import defaultdict


# initial naive solution
def isAnagram(s: str, t: str) -> bool:
    letter_counts = defaultdict(int)
    for letter in s:
        letter_counts[letter] += 1

    for letter in t:
        letter_counts[letter] -= 1
        if letter_counts[letter] < 0:
            return False

    return sum(letter_counts.values()) == 0


# add early returns
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letter_counts = defaultdict(int)
    for letter in s:
        letter_counts[letter] += 1

    for letter in t:
        letter_counts[letter] -= 1
        if letter_counts[letter] < 0:
            return False

    return sum(letter_counts.values()) == 0


# most compact solution
def isAnagram3(s: str, t: str) -> bool:
    counts = {c: (s.count(c) - t.count(c) == 0) for c in set(s + t)}
    return all(counts.values())


from collections import defaultdict



# of 6 solutions posted on leetcode, this aligns with #5. there is one more optimization I can make.
# don't get it yet. TODO: understan solution #6
def checkInclusion(s1: str, s2: str) -> bool:
    match_chars = defaultdict(int)
    for c in s1:
        match_chars[c] += 1

    l = 0
    r = 0
    while r < len(s2):
        if s2[r] in match_chars:
            match_chars[s2[r]] -= 1

        if all([val == 0 for val in match_chars.values()]):
            return True

        if r - l + 1 == len(s1):  # we are at our max str len
            if s2[l] in match_chars:
                match_chars[s2[l]] += 1
            l += 1

        r += 1

    return False

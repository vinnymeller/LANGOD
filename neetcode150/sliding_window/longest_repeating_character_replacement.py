# FIXME: solution doesn't work, passes 24/41 test cases
def characterReplacement(s: str, k: int) -> int:
    l = 0
    r = 0
    replaced_idxs = []
    longest = 0

    while r < len(s):
        if s[r] == s[l]:
            pass
        else:
            if (
                len(replaced_idxs) == k
            ):  # we've used all our replacements, move l and r to 1st replace idx
                if k > 0:
                    l = r = replaced_idxs[0]
                    replaced_idxs = []
                else:
                    l = r
            else:
                replaced_idxs.append(r)
        length = r - l + 1
        longest = max(length, longest)
        r += 1

    return longest

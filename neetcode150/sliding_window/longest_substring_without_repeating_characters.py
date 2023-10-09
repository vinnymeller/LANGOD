from typing import Dict


# Took 2 tries, originally messed up where i move the left index to
# at first moved it to the right pointer to restart, but im actually
# obviously supposed to move it to the index after where the last instance
# of the repeated character occurred. need to pay more attention to what im doing
# with my window
def lengthOfLongestSubstring(s: str) -> int:
    indexes: Dict[str, int] = {}

    l = r = 0
    longest_substr = 0

    while r < len(s):
        if s[r] not in indexes or indexes[s[r]] < l:
            substr_len = r - l + 1
            longest_substr = max(longest_substr, substr_len)
        else:
            l = indexes[s[r]] + 1

        indexes[s[r]] = r
        r += 1

    return longest_substr

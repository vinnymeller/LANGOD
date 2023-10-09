from collections import defaultdict
from typing import List


# my 1st try i managed lists of bools instead of sets, but i had an issue that i
# apparently kept glossing over. switched to this and it worked 1st try.
# i still wanna know what i did wrong before but ill ignore it for now, probably something dumb
# keep in mind for later - managing indexes manually = messed up, just using defaultdict to manage them = easy
def isValidSudoku(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            value = board[r][c]

            if value == ".":
                continue

            if value in rows[r] or value in cols[c] or value in boxes[(r // 3, c // 3)]:
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[(r // 3, c // 3)].add(value)

    return True

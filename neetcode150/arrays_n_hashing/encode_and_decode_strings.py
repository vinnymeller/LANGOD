from typing import List


def encode(strs: List[str]) -> str:
    encoded_str = ""
    for s in strs:
        encoded_str += str(len(s)) + "#" + s

    return encoded_str


# my initial solution I tried using `find` method but clearly got the api wrong and had issues
# just stick to easy while loops instead of using fancy stuff unless im 100% sure i know it
def decode(s: str) -> List[str]:
    strs = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        len_end = int(s[i:j])

        strs.append(s[j + 1 : j + 1 + len_end])
        i = j + len_end + 1

    return strs

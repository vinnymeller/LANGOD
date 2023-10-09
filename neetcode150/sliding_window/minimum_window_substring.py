from collections import defaultdict


# solution, passes testcases, but is only faster than 15%
# clearly not the optimal solution
# TODO: figure out how the hell to do this in O(n+m)
# this solution should be uhhhh... O(n*m) I think ?
# checks m dictionary values 2n times (?)
# idk. i seemingly suck at sliding window problems. rarely am coming up with ideal solutions
# happy that i got any working solution in a few mins but I cannot think of how to O(n+m) it
def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    t_counts = defaultdict(int)
    for c in t:
        t_counts[c] += 1

    min_substr = ""

    l = 0
    r = 0

    while r < len(s):
        have_substr = False
        if s[r] in t_counts:
            t_counts[s[r]] -= 1

        while all([val <= 0 for val in t_counts.values()]):
            # now move the left ptr over until this no longer holds
            if s[l] in t_counts:
                t_counts[s[l]] += 1
            l += 1
            have_substr = True

        if have_substr:
            substr = s[l - 1 : r + 1]
            if not min_substr or len(substr) < len(min_substr):
                min_substr = substr

        r += 1

    return min_substr

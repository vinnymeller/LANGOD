from typing import List

# got 1st try pretty much instantly, *dont* need review on this one
def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1

    max_area = 0

    while l < r:
        
        lh = height[l]
        rh = height[r]

        min_height = min(lh, rh)

        area = min_height * (r - l)

        max_area = max(max_area, area)

        if lh <= rh:
            l += 1
            while l < r and lh >= height[l]:
                l += 1
        else:
            r -= 1
            while l < r and rh >= height[r]:
                r -= 1

    return max_area



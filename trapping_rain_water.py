from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_left = height[l]
        max_right = height[r]

        total = 0

        while l < r:
            cur_vol = 0
            if max_left <= max_right:
                l += 1
                cur_vol = max(0, max_left - height[l])
                max_left = max(max_left, height[l])
            else:
                r -= 1
                cur_vol = max(0, max_right - height[r])
                max_right = max(max_right, height[r])

            total += cur_vol

        return total

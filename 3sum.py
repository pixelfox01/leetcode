from typing import List


class solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1

        return [list(i) for i in result]

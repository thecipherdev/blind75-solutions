from typing import List

# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[val] = i
        return []


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))

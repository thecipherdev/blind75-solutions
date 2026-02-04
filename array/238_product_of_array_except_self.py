from typing import List

# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multiplier = 1
        right_multiplier = 1
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(len(nums)):
            j = -i - 1
            left[i] = left_multiplier
            right[j] = right_multiplier
            left_multiplier *= nums[i]
            right_multiplier *= nums[j]

        return [left_val * right_val for left_val, right_val in zip(right, left)]


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))

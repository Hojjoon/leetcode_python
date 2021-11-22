class Solution:
    # noinspection PyMethodMayBeStatic
    def two_sum(self, nums: list, target: int) -> list:

        indexed = {v: i for i, v in enumerate(nums)}

        for i in nums:
            if target - i in indexed and (nums.index(i) != indexed[target - i]):
                return [nums.index(i), indexed[target - i]]



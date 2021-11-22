class Solution:
    # noinspection PyMethodMayBeStatic
    def array_pair_sum(self, nums: list) -> int:

        nums.sort()
        sums = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                sums += nums[i]

        return sums

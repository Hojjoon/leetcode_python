class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
        sums = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                sums += nums[i]

        return sums

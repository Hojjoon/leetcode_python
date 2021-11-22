class Solution:
    def three_sum(self, nums: list) -> list:

        discovered = []
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i] and [nums[i], nums[left], nums[right]] not in discovered:
                    discovered.append([nums[i], nums[left], nums[right]])
                    left += 1
                    continue
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    left += 1
                    continue

        return discovered

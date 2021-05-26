class Solution:
    def solve(self, nums):
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new_nums.append(nums[i])
        for j in range(len(nums)):
            if nums[j] == 0:
                new_nums.append(nums[j])
        return new_nums
        
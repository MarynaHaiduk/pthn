class Solution:
    # solution1
    # def twoSum(self, nums, target):
    #     for i in range(0, len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # solution2
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]

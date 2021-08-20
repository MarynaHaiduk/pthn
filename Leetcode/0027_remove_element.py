class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))  # 2
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums

test = [1,2,3,4,5,7]
t = Solution()
a = t.runningSum(test)
print(a)

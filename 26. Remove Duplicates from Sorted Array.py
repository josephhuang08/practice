class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k

nums = [0,0,1,1,1,2,2,3,3,4]
ans = Solution()

k = ans.removeDuplicates(nums)
print(k)

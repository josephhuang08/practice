class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return i, hashmap[target - num]
            hashmap[num] = i
        return []

nums = [2,7,11,15]
target = 9

a = Solution()
out = a.twoSum(nums, target)
print(out)
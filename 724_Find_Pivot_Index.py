class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for pivot in range(0, len(nums)):
            right_sum -= nums[pivot]

            if left_sum == right_sum:
                return pivot
                
            left_sum += nums[pivot]
        
        return -1
    

nums = [2,1,-1]
a = Solution()
print(a.pivotIndex(nums))

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend the subarray or start new
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        local_max = 0
        global_max = nums[0]
        
        for i in nums:
            local_max = max(local_max+i, i)
            if local_max > global_max:
                global_max = local_max
        
        return global_max

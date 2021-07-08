class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                s = nums[i]+ nums[start] + nums[end]
                if abs(s - target) < abs(result - target):
                    result = s

                if s < target:
                    start +=1
                elif s > target:
                    end -=1
                else:
                    return result
        
        return result

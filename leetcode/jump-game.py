class Solution(object):
    def canJump(self, nums):
        #solution by Nick White
        lastGoodIndex = len(nums) -1
        
        #traversing backwards
        for i in range(len(nums)-1, -1, -1):
            if (nums[i] + i >= lastGoodIndex):
                lastGoodIndex = i
            
        return lastGoodIndex == 0

class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        #use neetcode youtuber algorithm: breadth first search (greedy approach)
        res = 0
        l = r = 0 
        
        while r < len(nums) - 1:
            farthest = 0
            
            #find the farthest jump range (to minimize jumps)
            for i in range(l, r+1):
                farthest = max(farthest, i+ nums[i])
            
            #find the next range
            #set l = r+1 as we don't want to miss any potential jump ranges (hence greedy)
            l = r+1
            r = farthest
            res +=1
        
        return res
            

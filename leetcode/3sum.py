class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #no need for backtracking
        #attempt result by shaysakazi
        
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        #the max index of start position is two indices before the last index
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                if nums[i]+ nums[start] + nums[end] == 0:
                    if [nums[i],nums[start],nums[end]] not in result:
                        result.append([nums[i],nums[start],nums[end]])
                    #change both start and end indices to prevent duplication
                    start +=1
                    end -=1
                elif nums[i]+ nums[start] + nums[end] < 0:
                    start +=1
                else:
                    end -=1
        
        return result
                    

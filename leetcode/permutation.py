class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # implementation of takeuForward YouTube channel 
        
        found = False
        
        #we will always swap the last number so skip it
        i = len(nums) - 2
        
        while i >= 0:
            if nums[i] < nums[i+1]:
                found = True
                break
            else:
                i -= 1
        
        #if this is the largest permutation, sort and return the array
        if not found:
            nums.sort()
        else:
            m = self.findMaxIndex(nums, nums[i], i)
            nums[i],nums[m] = nums[m],nums[i]
            #flip the remaining [::1] means flip
            nums[i+1:]= nums[i+1:][::-1]
            
    
    def findMaxIndex(self, n: List[int], num: int, idx: int) -> int:
        for i in range(len(n)-1, idx, -1):
            if n[i] > num:
                idx = i
                break
        
        return idx
                
            
        

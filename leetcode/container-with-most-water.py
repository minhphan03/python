class Solution:
    def maxArea(self, height: List[int]) -> int:
        #attempt solution by 5tigerjelly
        left = 0
        right = len(height)-1
        
        res = 0
        while left < right:
            res = max(res, (right-left)*min(height[left],height[right]))
            
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        
        return res

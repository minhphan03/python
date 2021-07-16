class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums)-1
                while left < right:
                    ans = nums[i]+nums[j]+nums[left]+nums[right]
                    if ans == target and [nums[i],nums[j],nums[left],nums[right]] not in solutions:
                        solutions.append([nums[i],nums[j],nums[left],nums[right]])
                        left +=1
                        right -=1
                    elif ans < target:
                        left +=1
                    else:
                        right -=1
        return solutions
                                          
                                          

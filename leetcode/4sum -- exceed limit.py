class Solution:
    
    def fourSum(self, nums_: List[int], target_: int) -> List[List[int]]:
        solutions_ = []
        answer_ = []
        nums_.sort()
        self.fSum(nums_,target_, solutions_, answer_, 0)
        return solutions_
        
   
    def fSum(self, nums: List[int], target: int, solutions:List[List[int]], answer: List[int], index: int):
        
        if len(answer) == 4 and sum(answer) == target:
            for i in range(len(solutions)):
                if sorted(answer) == solutions[i]:
                    return
            for n in answer:
                if answer.count(n) > nums.count(n):
                    return
            new_copy = []
            new_copy.extend(sorted(answer))
            solutions.append(new_copy)
            return

        elif len(answer) == 4 or index >= len(nums):
            return

        for i in range(index, len(nums)):
            answer.append(nums[i])
            self.fSum(nums, target, solutions, answer, index + 1)
            answer.pop()

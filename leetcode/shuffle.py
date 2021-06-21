class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        n = int(len(nums)/2)
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result

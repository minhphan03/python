class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        s,e = 0, len(nums)-1
        return self.binarysearch(nums, target, s, e)
    def binarysearch(self, arr, value, l, r):
        m = (l + r) // 2
        while l < r:
            if arr[m] == value:
                return m
            elif arr[m] > value:
                r = m
            else:
                l = m+1
            m = (l + r) // 2
        return m+1 if value > arr[m] else m

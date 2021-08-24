class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) ==1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
        
        #implement binary search
        return [self.binarysearch_left(nums, target, 0,len(nums)-1), self.binarysearch_right(nums,target,0,len(nums)-1)]
    
    def binarysearch_left(self, arr, value, l, r):
        #base case
        if r >= l:
            m = (l+r) //2
            if arr[m] == value:
                if (m-1) == -1 or arr[m-1] != value:
                    return m
                else:
                    return self.binarysearch_left(arr, value, l, m-1)
            elif arr[m] > value:
                return self.binarysearch_left(arr, value, l, m-1)
            else:
                return self.binarysearch_left(arr, value, m+1, r)
        else:
            return -1
    def binarysearch_right(self, arr, value, l, r):
        #base case
        if r >= l:
            m = (l+r) //2
            if arr[m] == value:
                if (m+1) == len(arr) or arr[m+1] != value:
                    return m
                else:
                    return self.binarysearch_right(arr, value, m+1, r)
            elif arr[m] > value:
                return self.binarysearch_right(arr, value, l, m-1)
            else:
                return self.binarysearch_right(arr, value, m+1, r)
        else:
            return -1

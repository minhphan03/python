class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #by alextoqc

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        s, e = 0, len(nums) - 1
        m = (s+e) // 2

        #find the pivot (biggest)
        while s < e and nums[m] <= nums[m + 1]:
            if nums[m] > nums[e]:
                s = m
            else:
                e = m
            m = (e + s) // 2

        left = nums[:m + 1]
        right = nums[m + 1:]

        # binary search
        if right[0] <= target <= right[-1]:
            l, r = 0, len(right) - 1
            ans = self.binarysearch(right, target, l, r)
            return (m + 1) + ans if ans != -1 else -1
        else:
            l, r = 0, len(left) - 1
            ans = self.binarysearch(left, target, l, r)
            return ans if ans != -1 else -1

    #geeksbygeeks recursive binary search
    def binarysearch(self, arr, value, l, r):
        #base case
        if r >= l:
            m = (l+r) //2
            if arr[m] == value:
                return m

            elif arr[m] > value:
                return self.binarysearch(arr, value, l, m-1)
            else:
                return self.binarysearch(arr, value, m+1, r)
        else:
            return -1

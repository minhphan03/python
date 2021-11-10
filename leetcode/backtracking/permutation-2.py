class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = []
        def pm(n, s, l, r):
            if (l == r):
                if n not in s:
                    s.append(n[:])
            else:
                for i in range(l, r+1):
                    n[l], n[i] = n[i], n[l]
                    pm(n, s, l+1, r)
                    n[l], n[i] = n[i], n[l]
        
        pm(nums, s, 0, len(nums)-1)
        return list(s)

# runtime error (too long)
class Solution(object):
    def canJump(self, nums):
        # recursion ?
        if len(nums) == 1:
            return True

        def jump(num, i):
            if num[i] == 0:
                return
            if i + num[i] >= len(num) - 1:
                return True
            for n in range(1, num[i]+1):
                if jump(num, i+n) == True:
                    return True

            return False

        return jump(nums, 0)

class Solution:
    def countAndSay(self, n: int) -> str:
        # apparently I didn't understand what the problem was saying until I read the solutions
        
        # attempt by zhanz1
        
        #base case
        if n == 1:
            return "1"
        
        #recursion to the base case and continue from there
        nums = self.countAndSay(n-1)
        output = ""
        
        currCount = 0
        currNum = nums[0]
        
        # iterate through "count and say"
        for num in nums:
            if num == currNum:
                currCount +=1
            else:
                output += str(currCount) + currNum
                currCount = 1
                currNum = num
        return output + str(currCount) + currNum
                

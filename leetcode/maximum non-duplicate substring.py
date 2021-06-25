class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        max = 0
        for n in s:
            if n in result:
                result = result[(result.find(n))+1:]

            result += n

            if len(result) > max:
                max = len(result)

        return max

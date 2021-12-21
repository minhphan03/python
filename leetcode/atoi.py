# string to integer method on C/C++

class Solution:
    def myAtoi(self,s: str) -> int:
        isNeg = False
        n = 0
        result = 0
        while n < len(s):
            if s[n] != " ":
                if s[n].isnumeric():
                    result = result * 10 + int(s[n])
                elif s[n] == "-" or s[n] == "+":
                    if s[n] == "-":
                        isNeg = True
                else:
                    break
                if n + 1 < len(s) and (s[n + 1] in [" ", "+", "-"]):
                    break
            n += 1

        if isNeg:
            if result >= 2 ** 31:
                result = -2 ** 31
            else:
                result = -result
        elif result >= 2 ** 31:
            result = 2 ** 31 - 1
        return result

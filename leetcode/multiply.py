class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # attempt solution using elementary multiplication algorithm
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1), len(num2)
        res = [0]*(n1+n2)

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # minus the string 0
                res[i + j + 1] += (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] = res[i + j + 1] % 10
        result = ''
        if res[0] != 0:
            result += str(res[0])
        for i in range(1,len(res)):
            result += str(res[i])
        return result

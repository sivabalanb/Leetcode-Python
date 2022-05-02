#https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        str_num = sorted(str(num))
        num1 = int(str_num[0] + str_num[2])
        num2 = int(str_num[1] + str_num[3])
        
        return num1+num2
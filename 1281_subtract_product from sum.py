#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumn = 0
        for num in str(n):
            product *= int(num)
            sumn += int(num)
        return product - sumn
        
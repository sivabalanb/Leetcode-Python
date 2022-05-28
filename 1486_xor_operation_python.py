#https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = [start]
        sol = 0
        for _ in range(n-1):
            res.append(res[-1]+2)
            
        for n in res:
            sol = sol ^ n
        
        return sol
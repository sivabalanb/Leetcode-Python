#https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        for idx in range(len(str(num))-k+1):
            if int(str(num)[idx:idx+k]) != 0:
                if num % int(str(num)[idx:idx+k]) == 0:
                    count+= 1                
        return count
        
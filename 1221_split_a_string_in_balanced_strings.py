#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        from collections import deque
        q = deque()
        count = 0
        for c in s:
            if len(q) == 0:
                q.append(c)
                count+=1
            elif q[-1] == c:
                q.append(c)
            else:
                q.pop()            
        return count
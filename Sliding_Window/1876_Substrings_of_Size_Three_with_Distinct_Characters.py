#https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for idx in range(len(s)-2):           
            if len(set(s[idx:idx+3])) == 3:
                count += 1
        return count
                
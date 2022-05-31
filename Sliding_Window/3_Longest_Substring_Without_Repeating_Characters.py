#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left, my_set = 0, 0, set()
        
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            result = max(result, right - left + 1)
        return result
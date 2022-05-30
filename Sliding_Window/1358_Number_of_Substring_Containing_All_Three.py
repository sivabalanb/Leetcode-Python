#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result, left, count = 0, -1, {c:0 for c in 'abc'}
        
        for right, val in enumerate(s):
            count[val] += 1
            # print(f"Updating in dict {val} and updated {count[val]} dict {count}")
            while all(count.values()): #When its a valid pair with all val as 1
                #Once its a valid pair rest of the string is also valid
                result += len(s) - right
                #print(f"curr_str {s[left+1:right+1]} result {result} left {left} right {right} length {len(s)}")
                left += 1
                count[s[left]] -=1
        return result
                
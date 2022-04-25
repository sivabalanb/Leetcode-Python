#https://leetcode.com/problems/concatenation-of-array/
# 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums
        result.extend(nums)
        return result
        
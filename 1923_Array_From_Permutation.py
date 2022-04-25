#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(nums[num])
        return result
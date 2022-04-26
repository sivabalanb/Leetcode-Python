#https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for idx, num in enumerate(nums):
            if idx == 0:
                result.append(num)
            else:
                new_num = result[idx-1] + nums[idx]
                result.append(new_num)
        return result
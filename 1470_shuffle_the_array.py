#https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for idx, num in enumerate(nums):
            if idx < n:
                result.append(num)
                result.append(nums[idx+n])
            else:
                return result
            
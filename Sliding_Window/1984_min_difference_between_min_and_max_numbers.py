#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        
        curr_min = nums[-1]
        l, r = 0, k-1
        # for i in range(k, len(nums)):
        #     # res = min(res, nums[i] - nums[i - k + 1])
        #     curr_min = min(curr_min, nums[i] - nums[i-k+1])
        while r < len(nums):
            curr_min = min(curr_min, nums[r] - nums[l])
            l, r = l+1, r+1
        return curr_min
#https://leetcode.com/problems/maximum-average-subarray-i/submissions/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def calc(i):
            return sum(nums[i:i+k]) / k
        curr_sum = 0
        max_avg = float('-inf')
        for idx, val in enumerate(nums):
            curr_sum += val
            if idx >= k:
                curr_sum -= nums[idx-k]
            if idx >= k-1:
                max_avg = max(max_avg, curr_sum)
                        
        return max_avg / k
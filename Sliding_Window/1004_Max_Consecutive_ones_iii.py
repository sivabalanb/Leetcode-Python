#https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            # print(f" left {left} val {nums[left]} and right {right} val {nums[right]}")
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k+=1
                left += 1
        return right - left + 1
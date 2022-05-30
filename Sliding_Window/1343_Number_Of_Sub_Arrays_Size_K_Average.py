#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count, curr_sum = 0, 0
         
        for i in range(0,k-1):
            curr_sum += arr[i]
        # print(f"current sum {curr_sum}")
        
        for idx in range(k-1, len(arr)):
            curr_sum += arr[idx]
            # print(f" curr sum loop {curr_sum} removing index {idx-k+1} val {arr[idx-k+1]}")
            if curr_sum / k >= threshold: count+=1
            curr_sum -= arr[idx-k+1]
        return count
        
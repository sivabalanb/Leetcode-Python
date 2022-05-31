#https://leetcode.com/problems/sliding-window-maximum/

'''
Monotonic deque

https://algo.monster/problems/sliding_window_maximum
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        q = deque()
        res =[]
        for i, value in enumerate(nums):
            while q and nums[q[-1]] <= value:                
                print(f"\t popping {q[-1]} as numsq {nums[q[-1]]} <= {value}")
                q.pop()                                
            q.append(i)
            print(f"i {i} q {q} and val {value} ")
            if q[0] == i-k:
                q.popleft()
                print(f"q afer popping {q}")
            if i >= k-1:
                print(f"\t\tAppendnig {nums[q[0]]} to res {res} in iteration {i}" )
                res.append(nums[q[0]])
        return res
        
        
        
        #import heapq
        # curr_max, left = 0, 0
        # result=[]
        # for right in range(len(nums)-k+1):
        #     # print("curr widow", nums[left:right+k])
        #     # curr_max = max(nums[left:right+k])
        #     # print(heapq.heapify(nums[left:right+k]))
        #     # print(heapq.nlargest(1,nums[left:right+k])[0])
        #     heap_r = heapq.nlargest(1,nums[left:right+k])[0]
        #     result.append(heap_r)
        #     # print(f"curr_max {curr_max} and result {result}")
        #     left += 1
        # return result
            
        
#https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = { 0: 1 }
        cnt = res = 0
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                cnt += 1
            if cnt - k in dic:
                res += dic[cnt-k]
                # print(f"Updating result {res} as {cnt-k}")
            dic[cnt] = dic.get(cnt, 0) + 1
            # print(f"idx {idx} num {num} cnt {cnt} res {res} dic {dic}")
        return res
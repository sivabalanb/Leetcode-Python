#https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        it = iter(nums)
        for x, y in zip(it, it):
            result.extend([y]*x)
            
        return result
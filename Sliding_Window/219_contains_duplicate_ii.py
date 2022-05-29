#https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        
        for idx, val in enumerate(nums):
            print(f"idx {idx} and val {val} and hash {hash_map}")
            if val in hash_map and idx - hash_map[val] <= k:
                return True
            hash_map[val] = idx
            
        return False
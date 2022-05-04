#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        hash_map = {}
        #Knows Cases
        hash_map[max(nums)] = len(nums) - nums.count(max(nums))
        hash_map[min(nums)] = 0
        for i, numi in enumerate(nums):
            count = 0
            if numi not in hash_map:
                for j , numj in enumerate(nums):
                    if i!= j and nums[j] < nums[i]:
                        count+= 1
            else:
                count = hash_map[numi]
            hash_map[numi] = count
            result.append(count)
        return result
                
            
        
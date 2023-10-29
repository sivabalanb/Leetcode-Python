#https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Creating an dict to store hash map
        hash_map = {}

        # Enumerate through the given array to form the hash_map
        for i, num in enumerate(nums):

            # Calculate complement
            complement = target - num

            # Check if complement is already in hash
            if complement in hash_map:
                return (hash_map[complement], i)
            
            hash_map[num] = i


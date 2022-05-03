#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies) - extraCandies
        for x in candies:
            if  x >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result
        
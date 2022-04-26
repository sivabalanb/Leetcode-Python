#https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        for account in accounts:
            wealth = sum(account)
            result.append(wealth)
        return max(result)
            
        
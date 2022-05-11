#https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        map_k = {'type': 0, 'name': 2, 'color': 1}
        key = map_k[ruleKey]
        count = 0
        for item in items:
            if ruleValue == item[key]:
                count += 1
        return count
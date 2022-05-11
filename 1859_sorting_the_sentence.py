#https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(" ")
        res = ['x']*len(l)
        for i in l:
            res[int(i[-1])-1] = i[:-1]
        return " ".join(res)
        
        
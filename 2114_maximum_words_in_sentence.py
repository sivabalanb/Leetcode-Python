#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = []
        for sentence in sentences:
            wc = sentence.split(" ")
            result.append(len(wc))
        return max(result)
            
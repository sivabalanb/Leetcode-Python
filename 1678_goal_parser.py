#https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        my_parser = {'G' : 'G', '()' : 'o', '(al)': 'al'}
        result = ''
        stack = ''
        for c in command:
            stack += c
            if my_parser.get(stack) != None:
                result+=my_parser[stack]
                stack = ''
        return result
        
        
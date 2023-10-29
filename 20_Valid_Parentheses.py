# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # USe stack 
        stack = []
        # Match with existing stak
        valid_char = {')':'(', '}':'{', ']':'['}

        # Iterate through given string
        for char in s:
            if char in valid_char:
                top_element = stack.pop() if stack else '#'
                if top_element != valid_char[char]:
                    return False
            else:
                stack.append(char)
        return not stack

        
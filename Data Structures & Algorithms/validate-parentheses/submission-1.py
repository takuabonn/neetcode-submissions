class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lp = 0
        open_bracket = {
            '(':')',
            '{':'}',
            '[':']',
        }
        while lp < len(s):
            if len(stack) == 0:
                stack.append(s[lp])
            else:
                bracket = stack[len(stack)-1]
                if bracket in open_bracket and open_bracket[bracket] == s[lp]:
                    stack.pop()
                else:
                    stack.append(s[lp])
            lp += 1
        return len(stack) == 0
                


            

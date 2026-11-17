class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_brackets = {'(','[','{'}
        right_brackets = {')',']','}'}

        if s[0] in right_brackets:
            return False
        stack.append(s[0])

        for ii in range(1,len(s)):
            if s[ii] in left_brackets:
                stack.append(s[ii])
            else:
                if not stack:
                    return False
                left = stack.pop()
                if not (
                    (left == '(' and s[ii] == ')') 
                    or (left == '[' and s[ii] == ']') 
                    or (left == '{' and s[ii] == '}')
                ):
                    return False
        
        if stack:
            return False

        return True
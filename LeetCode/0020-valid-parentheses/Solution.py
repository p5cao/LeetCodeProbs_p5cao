class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in closeToOpen: # char in keys
                if not stack or stack.pop()!= closeToOpen[char]:
                    # return False if stack is empty or pair not matching
                    return False
            else:
                stack.append(char)
        
        return not stack
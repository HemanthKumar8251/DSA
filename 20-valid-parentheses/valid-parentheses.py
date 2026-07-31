class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '[{(':
                stack.append(p)
            else:
                if not stack:
                    return False
                if p==']' and stack.pop()=='[':
                    continue
                if p==')' and stack.pop()=='(':
                    continue
                if p=='}' and stack.pop()=='{':
                    continue
                return False
        if not stack:
            return True
        else:
            return False
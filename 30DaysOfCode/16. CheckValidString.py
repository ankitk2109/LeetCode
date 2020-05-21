# For concept understanding: https://www.youtube.com/watch?v=KuE_Cn3xhxI
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []

        for i in range(len(s)):
            c = s[i]
            if c == '*':
                star.append(i)
            if c== '(':
                stack.append(i)    
            if c == ')':
                if len(stack)==0 and len(star)==0:
                    return False
                elif stack:
                    stack.pop()
                else:
                    star.pop()
        
        if stack == []:
            return True
        
        if len(stack) > len(star):
            return False
        
        while(stack):
            tmpopen,tmpstar = stack.pop(),star.pop()
            if tmpstar < tmpopen:
                return False
        return True
            
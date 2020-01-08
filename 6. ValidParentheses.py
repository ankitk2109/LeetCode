#Problem Statement available at: https://leetcode.com/problems/valid-parentheses/

#Approach 1: optimised
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {']':'[',')':'(','}':'{'}
        stack = []

        for ele in s:
            if ele in dic:
                if(stack != [] and dic[ele]==stack[-1]):
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
                
                
        if(stack == []):
            return True
        
        else:
            return False
'''
#Approach 2
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'[':']','{':'}','(':')',']':'[',')':'(','}':'{'}
        stack = []
        size = len(s)
        
        if ( s == ''):
            return True
        
        stack.append((s[0]))
        
        for i in range(1,size):
            if(stack == []):
                stack.append(s[i])
            elif(dic[stack[-1]] == s[i] ):
                stack.pop()
            else:
                stack.append(s[i])
                
        if(len(stack) ==0):
            return True
        
        else:
            return False
'''
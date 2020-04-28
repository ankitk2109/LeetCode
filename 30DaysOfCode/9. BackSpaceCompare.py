class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in range(len(S)):
            if len(stack_s) != 0 and S[i] == '#':
                stack_s.pop()
            if S[i] !='#':
                stack_s.append(S[i])
        
        for i in range(len(T)):
            if len(stack_t) != 0 and T[i] == '#':
                stack_t.pop()
            if T[i] !='#':
                stack_t.append(T[i])
        return(stack_s == stack_t)
                    
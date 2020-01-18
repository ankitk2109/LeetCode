#Problem Statement available at: https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(s is not ""):
            s_lst = s.split(' ')
            n = len(s_lst)
            while(n>0):
                if(s_lst[n-1] is not ''):
                    return len(s_lst[n-1])
                n = n-1
            return 0
        else:
            return 0
                
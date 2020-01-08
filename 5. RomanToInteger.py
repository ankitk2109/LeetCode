#Problem available at: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        n = len(s)
        res = 0
        for i in range(n-1):
            if(dic[s[i]]<dic[s[i+1]]):
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
                
        res += dic[s[-1]]

        return res
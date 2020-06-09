class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)==0):
            return True
        i = 0
        j = 0
        while(j<len(t) and i < len(s)):
            if(s[i]==t[j]):
                i+=1
            j+=1
        return i==len(s)
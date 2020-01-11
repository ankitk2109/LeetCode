#Problem Statement available at: https://leetcode.com/problems/implement-strstr/submissions/s

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if (len(needle)==0): #If needle is empty we need to return 0. Also if haystack is empty we need to return -1
            return 0
        else:
            #Keeping length of both strings for simplicity
            len_haystack = len(haystack)
            len_needle = len(needle)
            i=0
            
            #Run loop till length of haystack and until the sustring(needle) length is less or equal than haystack.
            while(len_haystack and len_haystack >= len_needle):
                if(haystack[i] == needle[0] and haystack[(i+len_needle)-1] == needle[-1]): #check first and last letter of needle in haystack. If they match then slice the substring from haystack and check if is equal to needle. 
                    temp = haystack[i:i+len_needle] #As we add len_needle to current index it is necesaary to check we don't exceed the length of haystack that's why we have added the other condition in while loop.
                    if(temp == needle): #If substring match with needle return index
                        return i
                i+=1
                len_haystack -= 1
                
        return -1
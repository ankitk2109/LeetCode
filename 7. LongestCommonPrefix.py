#Problem Statement available at: https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() #Once sorted we can simply check the first and last element. If the prefix is not present in last element then there is no common prefix.
        out = []
        if(len(strs)== 0): #If List is empty return empty string
            return ""
        elif(len(strs)==1): #If there is only one element in the list then return the element
            return strs[0]
        else:
            min_len = len(strs[0])
            for ele in strs: #Finding string with minimum length
                if(min_len>len(ele)):
                    min_len = len(ele)
            if(min_len>0): #Minimum length of the element should be greater then zero. For eg: ["",""] this is valid list having two elements both having len = 0
                first = strs[0]
                last = strs[-1]
                i=0
                while(i < min_len): #Looping till i is less then the minimum length 
                    if(first[i]==last[i]):
                        out.append(first[i])
                        i = i + 1
                    else:
                        break

                return "".join(out)
            else:
                return ""
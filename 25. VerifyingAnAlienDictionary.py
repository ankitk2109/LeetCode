#PS: https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wdic={}
        i=0
        for l in order:
            wdic[l] = i
            i += 1

        for i in range(len(words)-1):
            fword = words[i]
            sword = words[i+1]
            len_ = len(fword) if len(fword)<=len(sword) else len(sword) #Assigning Smaller Length
            
            j,k,flag = 0,0,0
            
            while(len_): #Loop till the smaller length
                
                if wdic[fword[j]] < wdic[sword[k]]: #If first letter is smaller than it's a valid sequence break the loop and check other pairs
                    break
                    
                elif wdic[fword[j]] > wdic[sword[k]]:   #If the second word is greater then it's an invalid sequence. Return False 
                    return False
                
                else:   #Equal; Check for other letters
                    j += 1
                    k += 1
                    flag = 1
                len_ -= 1
            
            if(flag == 1):  #If above loop ends bcoz the min length reached then we need to check which of the pair is smaller and if second word is smaller then it's an invalid sequence.
                if(len(fword)>len(sword)):
                    return False
                                        
        return True
            
#PS: https://leetcode.com/problems/occurrences-after-bigram
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        doc = text.split()
        output = []
        for i in range(len(doc)-2):
            if doc[i]==first and doc[i+1] == second:
                output.append(doc[i+2])
        return(output)
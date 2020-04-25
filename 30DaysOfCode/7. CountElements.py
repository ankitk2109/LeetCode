class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for ele in arr:
            if ele+1 in arr:
                count += 1
        return(count)
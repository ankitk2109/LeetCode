#Problem Statement available at: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_ = -1
        while(n):
            temp = arr[n-1]
            arr[n-1] = max_
            if(temp > max_):
                max_ = temp
            n -=1
        #print(arr)
        return arr
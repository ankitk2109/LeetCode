class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict_ = Counter(arr)
        count = 0
        for key in dict_.keys():
            if key+1 in dict_:
                count += dict_[key]
        return(count)
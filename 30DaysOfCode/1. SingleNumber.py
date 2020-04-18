class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = Counter(nums)
        for key in dict_:
            if dict_[key] == 1:
                return key
        
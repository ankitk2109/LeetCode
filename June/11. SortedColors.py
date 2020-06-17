class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        sorted_dict = dict(sorted(counter.items()))
        j = 0
        for key in sorted_dict.keys():
            for i in range(sorted_dict[key]):
                nums[j] = key
                j +=1
        
        return(nums)
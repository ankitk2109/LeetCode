class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        zipped = zip(nums,index)
        for x in zipped:
            output.insert(x[1],x[0])
        return output
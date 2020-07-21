class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if (len(nums)<=2):
            return nums
        output = []
        first = 0
        second = n
        while(first<n):
            output.append(nums[first])
            output.append(nums[second])
            first += 1
            second += 1
        return(output)
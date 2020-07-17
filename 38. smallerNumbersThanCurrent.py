class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = dict() # Store number of elemnts wich are less than smaller[i]	
        for i, n in enumerate(sorted(nums)):
            smaller[n] = smaller[n] if n in smaller else i

        return [smaller[n] for n in nums]
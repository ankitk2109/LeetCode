class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        prefix_sum = {}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
           
            if cur_sum == k:
                count +=1
            
            if cur_sum - k in prefix_sum:
                    count += prefix_sum[cur_sum - k]
            
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = 1
            else:
                prefix_sum[cur_sum] += 1

        return(count)
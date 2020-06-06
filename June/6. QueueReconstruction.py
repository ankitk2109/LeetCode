class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        final_queue = []
        
        sorted_heights = sorted(people, key = lambda x: (-x[0],x[1]))
        
        for x in sorted_heights:
            final_queue.insert(x[1],x)
        
        return final_queue
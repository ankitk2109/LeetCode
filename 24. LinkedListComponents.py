#PS: https://leetcode.com/problems/linked-list-components

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        sum_ = 0
        cur = head
        
        #We have to find the components that are sequentially connected for eg LL=[0,1,2,3,4,5,6] and G=[0,1,2,3,5,6] then there 2 connected components [0,1,2,3] and [5,6]. [4] is not considered as it is not present in G. so the output is 2
        while cur:
            if cur.val in G:
                sum_ +=1
                while cur is not None and cur.val in G:
                    cur = cur.next
            else:
                cur = cur.next
                
        return sum_
            
            
#PS: https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = ListNode(0)
        start.next = head
        prev = start
        cur = head
        
        while(cur):
            if(cur.val == val):
                prev.next = cur.next
            else:
                prev = cur             
            cur = cur.next
        return (start.next)
                
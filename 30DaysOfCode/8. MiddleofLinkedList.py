# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Edge Cases
        if head == None:
            return
        if head.next == None:
            return head
        if head.next.next == None:
            return head.next
        
        slow = fast = head
        #Finding middle element
        while(fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(fast.next == None):
                return slow
            if(fast.next.next == None):
                return slow.next
#PS: https://leetcode.com/problems/remove-linked-list-elements


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        
        else:
            cur = head
            prev = None
            
            while(cur):
                while(prev == None and cur.val == val):    #If first element = val and are repeated multiple times.
                    cur = cur.next
                    head = cur
                    if(cur == None):
                        return cur
                
                while(cur.val == val and prev != None):     #If its not a first element and are not repeated multiple times.
                    cur = cur.next
                    prev.next = cur
                    if(cur == None):
                        return head
            
                #Moving ahead if element doesn't match
                prev = cur
                cur = cur.next
            
            return head
                
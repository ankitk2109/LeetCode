#Problem Statement avialble at: https://leetcode.com/problems/merge-two-sorted-lists/submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:     
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = current = ListNode(None) #Creating a dummy node. But while returning result we only send linked list by skipping this dummy node

        while l1 and l2: #If both the linked list are not empty
            if l1.val <= l2.val:
                current.next = l1 #As the l1 points to the current node in linked list 1
                l1 = l1.next
            else: 
                current.next = l2 #As the l2 points to the current node in linked list 2
                l2 = l2.next

            current = current.next #Incrementing current after inserting new node from l1 or l2

        current.next = l1 or l2 #Assign the list which is not empty. Also after completion of while loop above both the list would be empty hence current.next at last would point to None. Also, this solves the edge case where both linked list are empty.
 
        return head.next #Skipping the dummy node
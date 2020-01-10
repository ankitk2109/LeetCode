#Problem Statement avialble at: https://leetcode.com/problems/merge-two-sorted-lists/submissions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:     
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 == None and l2 == None): #If both the linked List are empty return none
            return
        elif(l1==None): #If only l1 is empty then return l2
            return l2
        elif(l2==None): #If only l2 is empty then return l1
            return l1
        else:
            lst1=[], lst2=[]
            
            while(l1): #Appending all elements of linked list 1 to list 1
                lst1.append(l1.val)
                l1 = l1.next
                
            while(l2): #Appending all elements of linked list 2 to list 2
                lst2.append(l2.val)
                l2 = l2.next
                
            lst = lst1+lst2 #Combining both the list and the sort them.
            lst.sort()  
            
            node = ListNode(lst[0]) #Creating the first node.
            start = node #Pointing the start pointer at the head of the linked list. 
            current = start #Creating a current pointer that would be used to point to current processing node and joining link.
            
            #Below we are creating the linked list and joining them
            for i in range(1,len(lst)):
                node = ListNode(lst[i])
                current.next = node
                current = node
            
            #Returning the finally the start pointer
            return start
                
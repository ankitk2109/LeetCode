#Problem Statement available at: https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def createNode(self, val, current, carry):
        if(val>9):
            r = val % 10
            q = val // 10
            temp = ListNode(r)
            carry = q
            current.next = temp
        else:
            temp = ListNode(val)
            current.next = temp
        return current,carry

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1==None and l2==None):
            return
        elif(l1==None):
            return l2
        elif(l2 == None):
            return l1
        else:
            carry = 0
            head = ListNode(None)
            current = head
            while(l1 and l2):
                val = l1.val + l2.val + carry
                carry = 0
                current,carry = self.createNode(val,current,carry)
                l1 = l1.next
                l2 = l2.next
                current = current.next

            if l1:
                while(l1):
                    val = l1.val + carry
                    carry = 0
                    current,carry = self.createNode(val,current,carry)
                    l1 = l1.next
                    current = current.next
            if l2:
                while(l2):
                    val = l2.val + carry
                    carry = 0
                    current,carry = self.createNode(val,current,carry)
                    l2 = l2.next
                    current = current.next

            if(carry):
                temp = ListNode(carry)
                current.next = temp

            head = head.next
            return(head)
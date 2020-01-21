#Problem statement available at: https://leetcode.com/problems/middle-of-the-linked-list

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        cur = head
        len_lst = 0
        while(cur):
            len_lst += 1
            cur = cur.next

        for i in range(len_lst //2):
            head = head.next

        #print(head.val)
        return head
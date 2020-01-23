#Problem Statement available at:https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        else:
            queue = []
            sum_lst = []
            
            queue.append(root)
            
            while(queue):
                node = queue.pop()
                
                if(node.val >= L and node.val<= R):
                    sum_lst.append(node.val)
                
                #Add the subnode only if current node value is greater then left range and less then right range
                if node.left and node.val >= L: 
                    queue.append(node.left)
                
                if node.right and node.val <= R:
                    queue.append(node.right)
            
            #print (sum(sum_lst))
            return sum(sum_lst)
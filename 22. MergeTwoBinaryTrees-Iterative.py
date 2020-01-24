#PS: https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        if not t1:
            return t2
        if not t2:
            return t1
        else:
            stack = []
            stack.append((t1,t2))
            
            while(stack):
                n1,n2 = stack.pop()
                n1.val += n2.val
                
                #If n1.left is None we simply point to n2.left (Even if n2.left is None that would suffice our condition)
                if(n1.left == None):
                    n1.left = n2.left
                #if above condition is false that means n1.left is not none hence we check wether n2.left is none or not. If it's not none then append it to stack.    
                elif(n2.left != None):
                    stack.append((n1.left, n2.left))
                
                #If n1.right is None we simply point to n2.right (Even if n2.right is None that would suffice our condition)
                if(n1.right == None):
                    n1.right = n2.right
                
                #if above condition is false that means n1.right is not None hence we check wether n2.right is None or not. If it's not None then append it to stack. 
                elif(n2.right != None):
                    stack.append((n1.right, n2.right))  
        return t1

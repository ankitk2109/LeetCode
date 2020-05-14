# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def traverse(node):
            
            if not node: 
                return 0
            
            #the max depth go left from this node
            #the max depth go right from this node
            left = traverse(node.left)
            right = traverse(node.right)
            
            #update diameter if left+right is bigger
            self.diameter = max(self.diameter, left+right)
            
            #add 1 is for the step that get to this node
            #max(left, right) is for the left or right path that goes to the deepest
            return max(left, right)+1
        
        #iterate through the tree
        traverse(root)
        return self.diameter
        
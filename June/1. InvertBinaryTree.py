# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    	#idea is to create a mirror image of the original binary tree
    	#Go in post-order traversal and swap the leaf nodes.
        if root== None:
            return None

        left = self.invertTree(root.left) #reach at the left leaf node. Note:At start of recurssion
        right = self.invertTree(root.right)	#reach to the right leaf node. Note:At start of recurssion
        
        #Swap the two pointers
        root.right = left
        root.left = right
        return root
            
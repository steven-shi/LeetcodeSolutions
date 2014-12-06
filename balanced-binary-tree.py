'''
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.depth(root)[1]

        
    def depth(self, root):
        if root is None:
            return (0, True)
        left = self.depth(root.left)
        if left[1] == False:
            return (None,False)
        right = self.depth(root.right)
        if right[1] == False:
            return (None, False)
        if abs(left[0] - right[0]) > 1:
            return (None,False)
        else:
            return (max(left[0]+1, right[0]+1), True)
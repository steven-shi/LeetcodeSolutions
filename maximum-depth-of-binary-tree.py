'''
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return 1
        if root.left == None:
            return self.maxDepth(root.right) + 1
        if root.right == None:
            return self.maxDepth(root.left) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


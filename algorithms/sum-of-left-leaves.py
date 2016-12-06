#404. Sum of Left Leaves
#
#Find the sum of all left leaves in a given binary tree.
#
#Example:
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recusive(self, root, isleft):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val if isleft else 0
        return self.recusive(root.left, True) + self.recusive(root.right, False)
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recusive(root, False)
        


 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
  def inorderTraversal(self,root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

tree1 = TreeNode(1)
tree1.left = TreeNode(None)

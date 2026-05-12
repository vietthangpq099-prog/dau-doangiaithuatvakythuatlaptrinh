# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root or root.val == val:
            return root
            
        # Neu gia tri can tim nho hon gia tri nut hien tai -> Re trai
        if val < root.val:
            return self.searchBST(root.left, val)
        # Neu gia tri can tim lon hon gia tri nut hien tai -> Re phai
        return self.searchBST(root.right, val)
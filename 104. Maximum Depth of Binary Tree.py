# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
            
        # De quy di tim do sau cua nhanh trai va nhanh phai
        do_sau_trai = self.maxDepth(root.left)
        do_sau_phai = self.maxDepth(root.right)
        # Chon nhanh sau hon va cong them 1 (tinh ca nut hien tai)
        return max(do_sau_trai, do_sau_phai) + 1
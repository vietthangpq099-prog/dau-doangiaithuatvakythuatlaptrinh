# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        tong = 0
        # Kiem tra xem con trai cua nut hien tai co ton tai VA co phai la nut la khong
        if root.left and not root.left.left and not root.left.right:
            # Neu dung, cong gia tri cua nut la trai nay vao tong
            tong += root.left.val
        # Tiep tuc de quy xuong nhanh trai va nhanh phai de cong don ket qua
        tong += self.sumOfLeftLeaves(root.left)
        tong += self.sumOfLeftLeaves(root.right)
        return tong
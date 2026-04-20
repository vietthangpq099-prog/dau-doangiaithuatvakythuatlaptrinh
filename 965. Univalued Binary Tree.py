# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        gia_tri_goc = root.val

        def dfs(node):
            # Neu di den cuoi duong (rong) ma chua phat hien loi, tra ve True
            if not node:
                return True
            # Neu phat hien 1 nut co gia tri khac voi tieu chuan, lap tuc bao Sai
            if node.val != gia_tri_goc:
                return False
            # Tiep tuc kiem tra dong thoi ca 2 nhanh Trai va Phai
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
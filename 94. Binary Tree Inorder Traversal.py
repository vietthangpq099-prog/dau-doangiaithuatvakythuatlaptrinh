# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        # Lap chung nao con tro chua tro den None hoac stack chua rong
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # Khi khong the di sang trai duoc nua, lay node tren cung cua stack ra
            curr = stack.pop()
            # Them gia tri cua node vao mang ket qua (Xu ly nut goc)
            result.append(curr.val)
            # Chuyen huong sang xu ly nhanh ben phai
            curr = curr.right
        return result
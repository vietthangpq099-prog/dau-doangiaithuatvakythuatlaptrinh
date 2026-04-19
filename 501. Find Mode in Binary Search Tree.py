# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        # Khoi tao cac bien toan cuc de theo doi trong qua trinh de quy
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.modes
        
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        
        # Xu ly nut Goc (Hien tai)
        if node.val == self.current_val:
            self.current_count += 1
        else:
            self.current_val = node.val
            self.current_count = 1
        # So sanh voi ky luc max_count
        if self.current_count > self.max_count:
            self.max_count = self.current_count
            self.modes = [node.val] # Xoa ky luc cu, tao ky luc moi
        elif self.current_count == self.max_count:
            self.modes.append(node.val) # Dong hang ky luc, them vao mang
        self.inorder(node.right)
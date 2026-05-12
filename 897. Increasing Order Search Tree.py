# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.dummy = TreeNode(0)
        self.current = self.dummy
        # Ham de quy duyet In-order (Trai -> Goc -> Phai)
        def inorder(node):
            if not node:
                return
            # 1. Di xuong tan cung nhanh Trai
            inorder(node.left)
            # 2. Xu ly nut hien tai
            node.left = None                 
            self.current.right = node         
            self.current = self.current.right 
            # 3. Tiep tuc di xuong nhanh Phai
            inorder(node.right)
        # Kich hoat duyet cay
        inorder(root)
        # Tra ve cay moi, bo qua nut gia ban dau
        return self.dummy.right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        # 2. Neu chi co 1 cay rong, hoac gia tri cua 2 nut hien tai khac nhau -> Sai
        if not p or not q or p.val != q.val:
            return False
        # Chi tra ve True neu CA HAI nhanh deu giong nhau 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
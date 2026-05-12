# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaves(node, sequence):
            if not node:
                return
            # Neu la nut la (khong co ca con trai va con phai)
            if not node.left and not node.right:
                sequence.append(node.val)
                return   
            # Uu tien duyet nhanh Trai truoc, nhanh Phai sau
            get_leaves(node.left, sequence)
            get_leaves(node.right, sequence)
            
        seq1 = []
        seq2 = []
        
        # Phat dong thu thap cho ca 2 cay
        get_leaves(root1, seq1)
        get_leaves(root2, seq2)
        # So sanh toan bo mang
        return seq1 == seq2
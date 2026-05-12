# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        
        # Ham de quy duyet cay
        def dfs(node):
            if not node:
                return False
            # Tinh so can tim de dat duoc tong k
            so_can_tim = k - node.val
            if so_can_tim in seen:
                return True
                
            # Neu chua co, them gia tri cua nut nay vao lich su
            seen.add(node.val)
            
            # Tiep tuc tim kiem tren ca 2 nhanh Trai va Phai
            return dfs(node.left) or dfs(node.right)
        # Kich hoat ham de quy tu nut goc
        return dfs(root)
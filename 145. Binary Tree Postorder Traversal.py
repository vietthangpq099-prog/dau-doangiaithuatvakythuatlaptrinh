# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            # Lay node tren cung ra (theo thu tu Goc -> Phai -> Trai)
            node = stack.pop()
            result.append(node.val)
            # Nhet Trai vao truoc (chim xuong day stack)
            if node.left:
                stack.append(node.left)
            # Nhet Phai vao sau (noi len tren de duoc pop ra xu ly truoc)
            if node.right:
                stack.append(node.right)
        return result[::-1]
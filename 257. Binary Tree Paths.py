# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        def dfs(node, path):
            if not node:
                return
            # Ghep gia tri cua node hien tai vao duong di
            path += str(node.val)
            
            if not node.left and not node.right:
                result.append(path)
            else:
                path += "->"
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
        # Goi ham DFS bat dau tu root, duong di ban dau la chuoi rong
        dfs(root, "")
        return result
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])     
        while queue:
            # "Chot so" so luong nut dang co trong hang doi o tang hien tai
            level_size = len(queue)
            current_level = []
            
            # Xu ly chinh xac level_size nut cua tang nay
            for _ in range(level_size):
                # Lay nut o dau hang doi ra
                node = queue.popleft()
                current_level.append(node.val)
                
                # Dua cac nut con vao hang doi cho tang tiep theo
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
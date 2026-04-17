# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])

        while queue:
            # Lay node dau tien ra khoi hang doi (vao truoc ra truoc)
            node, depth = queue.popleft()    
            # Kiem tra xem day co phai la nut la khong (khong co con)
            if not node.left and not node.right:
                return depth 
            # Neu co con trai, dua no vao hang doi de cho xet o tang tiep theo
            if node.left:
                queue.append((node.left, depth + 1))
            # Neu co con phai, dua no vao hang doi de cho xet o tang tiep theo
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
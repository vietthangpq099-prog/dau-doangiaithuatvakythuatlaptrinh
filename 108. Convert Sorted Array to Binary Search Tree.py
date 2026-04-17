# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def xay_dung(left, right):
            if left > right:
                return None 
            # Tim vi tri o giua de lam nut goc (giup cay can bang)
            mid = left + (right - left) // 2
            # Tao nut goc voi gia tri o giua
            root = TreeNode(nums[mid])
         
            root.left = xay_dung(left, mid - 1)
            root.right = xay_dung(mid + 1, right)
            return root
        return xay_dung(0, len(nums) - 1)
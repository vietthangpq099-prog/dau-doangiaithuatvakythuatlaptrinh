class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        vi_tri_chen = 0 
        for i in range(len(nums)):
            # Nếu phát hiện số khác 0
            if nums[i] != 0:
                # Hoán đổi nó về vị trí chờ, sau đó nhích vị trí chờ lên
                nums[vi_tri_chen], nums[i] = nums[i], nums[vi_tri_chen]
                vi_tri_chen += 1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        # Lặp chừng nào khoảng tìm kiếm vẫn còn hợp lệ
        while left <= right:
            # Tìm vị trí ở giữa (dùng phép chia lấy nguyên //)
            mid = left + (right - left) // 2
            # Nếu tìm thấy đích ở ngay giữa
            if nums[mid] == target:
                return mid
            
            # Nếu số ở giữa nhỏ hơn đích, đích ở nửa bên phải
            elif nums[mid] < target:
                left = mid + 1
            # Nếu số ở giữa lớn hơn đích, đích ở nửa bên trái
            else:
                right = mid - 1
        return -1
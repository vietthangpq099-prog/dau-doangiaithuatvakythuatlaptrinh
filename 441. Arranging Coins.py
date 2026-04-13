class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            # Tong so xu can thiet de xay duoc mid hang
            coins_needed = mid * (mid + 1) // 2
            if coins_needed == n:
                return mid
            elif coins_needed > n:
                # Neu can nhieu xu hon n, ta phai giam so hang xuong
                right = mid - 1
            else:
                # Neu can it xu hon n, ta thu tang so hang len de dung not xu du
                left = mid + 1
        return right
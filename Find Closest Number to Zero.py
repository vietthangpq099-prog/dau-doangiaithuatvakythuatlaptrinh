class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gan_nhat = nums[0]
        for so in nums:
            khoang_cach_hien_tai = abs(so)
            khoang_cach_gan_nhat = abs(gan_nhat)
            if khoang_cach_hien_tai < khoang_cach_gan_nhat:
                gan_nhat = so

            elif khoang_cach_hien_tai == khoang_cach_gan_nhat:
                if so > gan_nhat:
                    gan_nhat = so  
        return gan_nhat
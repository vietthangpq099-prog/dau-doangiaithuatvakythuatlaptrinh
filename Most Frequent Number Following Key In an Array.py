class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        dem_so = {}
        so_lan_max = 0
        ket_qua = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                so_lien_sau = nums[i + 1]
                
                if so_lien_sau in dem_so:
                    dem_so[so_lien_sau] += 1
                else:
                    dem_so[so_lien_sau] = 1
                if dem_so[so_lien_sau] > so_lan_max:
                    so_lan_max = dem_so[so_lien_sau]
                    ket_qua = so_lien_sau        
        return ket_qua

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        so_nho_hon = 0
        so_bang = 0
        for so in nums:
            if so < target:
                so_nho_hon += 1
            elif so == target:
                so_bang += 1
        ket_qua = []
        for i in range(so_bang):
            ket_qua.append(so_nho_hon + i)
        return ket_qua
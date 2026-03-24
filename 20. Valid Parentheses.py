class Solution(object):
    def isValid(self, s):
        xep = []
        cho_ngoac = {')': '(', '}': '{', ']': '['}
        
        for ngoac in s:
            if ngoac in cho_ngoac:
                ngoac_mo_gan_nhat = xep.pop() if xep else '#'
                if cho_ngoac[ngoac] != ngoac_mo_gan_nhat:
                    return False
            else:
                xep.append(ngoac)
        return len(xep) == 0
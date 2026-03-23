class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        dem = 0
        for tu in words:
            if tu.startswith(pref):
                dem += 1
        return dem
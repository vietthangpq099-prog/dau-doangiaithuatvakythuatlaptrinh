class Solution(object):
    def longestCommonPrefix(self, strs):
        i=0
        strs.sort()
        one=strs[0]
        end=strs[-1]
        while i<len(one) and i<len(end) and one[i]==end[i]:
            i+=1
        return one[:i]
          

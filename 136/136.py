class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        for i in nums:
            p^=i
            
        return p

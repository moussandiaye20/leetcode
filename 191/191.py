class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=0
        for i in range(32):
            
            if n& 1<<i :k+=1
        return k

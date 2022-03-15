class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=1
        k=1
        while i<n:
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
               
            i+=1
      
        return k

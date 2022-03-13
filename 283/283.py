class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        noZero=0
        n=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[noZero]=nums[i]
                noZero+=1
        
        while noZero<=len(nums)-1:
            nums[noZero]=0
            noZero+=1
        
        return nums
        

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=right=0
        
        while left<len(nums):
            if nums[left]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
            left+=1
        return nums

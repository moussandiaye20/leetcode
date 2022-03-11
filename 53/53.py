class Solution:
    def maxSubArray(self, nums):
        
        maxSum=nums[0]
        current=0
        
        for i in range(len(nums)):
            
            
            if current<0:
                current=0
            current+=nums[i]
            maxSum=max(current,maxSum)
        
        return maxSum

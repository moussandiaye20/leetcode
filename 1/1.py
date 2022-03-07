class Solution:
    def twoSum(self, nums, target ) :
        seen ={}
        
        for i,j in enumerate(nums):
            diff=target-j
            
            if diff in seen:
                return (seen[diff],i)
        
            seen[j]=i
         
        
        

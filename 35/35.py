class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        left,right=0,len(nums)-1
        middle=0
        while left<=right:
            middle=(right-left)//2+left
            
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                
                left=middle+1
                print(left,right)
            else:
                right=middle-1
            
        return left
  
      

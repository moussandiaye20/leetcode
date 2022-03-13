class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
               
                nums[i]='_'
            else: k+=1
        size=len(nums)-1
      
        left=right=len(nums)-1
        while left>=0:
            if nums[left]=='_':
                nums[right], nums[left]=nums[left],nums[right]
                right-=1
            
            left-=1
    
        print(nums)
                
        return k

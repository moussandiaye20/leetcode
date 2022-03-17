class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        num=set(range(1,len(nums)+1))
        
        for i in nums:
            if i in num:
                num.discard(i)
        
        
        return list(num)

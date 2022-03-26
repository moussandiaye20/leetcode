class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        if not nums:return -1,-1
        found=False
        start=end=0
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                found=True
                start=end=mid
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1


        if not found:return-1,-1
        while start>=0 and target==nums[start]:
            start-=1
        while end<len(nums) and target==nums[end]:
            end+=1

        return start+1,end-1

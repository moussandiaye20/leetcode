class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        size=len(arr)-1
        max_so_far=-1
        while size>=0:
            current=arr[size]
            arr[size]=max_so_far
            max_so_far=max(max_so_far,current)
            
            size-=1
            
        return arr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return 0
        
        start=-1
        lenght=len(haystack) 
        i=0
        l=len(needle)
        while i<=lenght: 
            if haystack[i:i+l]==needle:
            
                return i
                
              
            i+=1        
                        
          
         
        
        
        return start

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        last=0
        current=0
        size=len(s)-1
        while size>=0 and s[size]!=" ":
            last+=1
            size-=1
            
        return last 

class Solution:
    def isValid(self, s: str) -> bool:
        
        
        if len(s)%2!=0:return False
        
        stack =[]
        
        n=0
        size=len(s)
        while n<size:
            if s[n]=='(' or  s[n]=='{' or  s[n]=='[':
                stack.append(s[n])
            else:
                if not stack :return False
                c=stack.pop()
                print(c)
                if s[n]==')' and c!='(':return False
                if s[n]=='}' and c!='{':return False
                if s[n]==']' and c!='[':return False
                
            
            n+=1
        return stack==[]
        

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumO(n):
            if n<=9:return n*n
            return (n%10)*(n%10)+sumO(n//10)
        
        seen=set()
        while n!=1:
            n=sumO(n)
            if n in seen:
                print(n,seen)
                return False
            seen.add(n)
        
        
        
        return n==1

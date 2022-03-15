class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right=0,len(s)-1
        alpha="abcdefghijklmnopqrstuvwxyz0987654321"
        while left<=right:
            while left<right and s[left].lower() not in alpha:
                left+=1
            while left<right and s[right].lower() not in alpha:
                right-=1
            if left<right and s[right].lower()!=s[left].lower() :return False
            left+=1
            right-=1
        
        return True
                
            

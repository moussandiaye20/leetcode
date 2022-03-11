class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):return False
       
        s_=collections.defaultdict(lambda:0)
        t_=collections.defaultdict(int)
        
        for letter in s:
            s_[letter]+=1
        
        for letter in t:
            t_[letter]+=1
        
        for letter in s_:
            if s_[letter]!=t_[letter]:return False
        
        return True

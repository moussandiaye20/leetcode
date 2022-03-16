class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso_s={}
        iso_t={}
        if len(s)!=len(t):return False
        
        
        for i in range(len(s)):
            if s[i] not in iso_s and  t[i] not in iso_t:
                iso_s[s[i]]=t[i]
                iso_t[t[i]]=s[i]
            elif iso_s.get(s[i])!=t[i]  or iso_t.get(t[i])!=s[i]:
                return False
        return True
                

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=""
        
        for i in s:
            if ord("A")<=ord(i) and ord(i)<=ord("Z"):ss+=chr(ord(i)+32)
            else:
                ss+=i
        return ss

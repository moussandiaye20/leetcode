class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        results=set()
        for email in emails:
            local,domain=email.split("@")
            s=''
            for i in range(len(local)):
                if local[i]=='+':break
                if local[i]!='.':s+=local[i]
            print(s)
            results.add(s+'@'+domain)
                
        return len(results)

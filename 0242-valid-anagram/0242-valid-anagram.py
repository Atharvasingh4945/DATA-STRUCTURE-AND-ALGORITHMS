class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #me thinking to pick two loop and make i constant and move j if we didnt get the same value then false else true 
        #for i in range(0,len(s)):
        #    for j in range (i+1,len(s)):
        #        s[i]==s[j]
        #        return True
        #return False this will not work kyuki ex 2 dhekho r i pe hai and j bhi r ko find kr raha hai at the last index and jaise hi yeah hua it returns true 
        count={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if s[i] in count:
                count[s[i]]=count[s[i]]+1
            else:
                count[s[i]]=1
        for j in range(0,len(t)):
            if t[j]  not in count:
                return False

            count[t[j]]=count[t[j]]-1
            if count[t[j]]<0:
                return False
        return True

        
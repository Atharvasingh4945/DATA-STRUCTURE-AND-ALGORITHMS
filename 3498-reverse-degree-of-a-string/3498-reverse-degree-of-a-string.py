class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters="abcdefghijklmnopqrstuvwxyz"
        value=26
        mapping={}
        sum=0
        for letter in letters:
            mapping[letter]=value
            value-=1
        for i in range(len(s)):
            pro=(i+1)*mapping[s[i]]
            sum+=pro
        return sum
        '''isme i created a hashmap and unki mapping ulti krdi then ek new loop mai mapping value and index value ka product liya and then unka sum krwaya'''

        
        
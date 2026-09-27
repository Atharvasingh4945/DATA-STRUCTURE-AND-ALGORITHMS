class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return[]
        phone={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans=[]
        def backtrack(index,path):
            #index 2 and path kya hoga abc like that 
            if index==len(digits):
                ans.append(path)#add toh abc karogi index nhi karoge ie 12,3,4,4
                return
            ch=digits[index]
            letters=phone[ch]
            for letter in letters:
                backtrack(index+1,path+letter)
        backtrack(0,"")
        return ans




        
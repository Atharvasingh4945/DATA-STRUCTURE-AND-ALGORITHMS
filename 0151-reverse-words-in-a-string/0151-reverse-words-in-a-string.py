class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Remove leading and trailing spaces
        s = s.strip()

        # Split the string into words
        arr = s.split()

        # Store the answer
        ans = ""

        # Traverse from last word to first word
        for i in range(len(arr) - 1, -1, -1):
            ans = ans + arr[i] + " "

        # Remove the extra space at the end
        return ans.strip()
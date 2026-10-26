class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        ref = strs[0]                       # must be the FIRST word
        for i in range(len(ref)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or ref[i] != strs[j][i]:
                    return ref[:i]
        return ref
        
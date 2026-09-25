class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        self.i = 0
        s = expression

        def parseExpr():
            result = {""}
            while self.i < len(s) and s[self.i] not in ',}':
                term = parseTerm()
                result = {a + b for a in result for b in term}
            return result

        def parseTerm():
            if s[self.i] == '{':
                self.i += 1
                result = parseUnion()
                self.i += 1
                return result
            else:
                ch = s[self.i]
                self.i += 1
                return {ch}

        def parseUnion():
            result = parseExpr()
            while self.i < len(s) and s[self.i] == ',':
                self.i += 1
                result |= parseExpr()
            return result

        return sorted(parseExpr())
        
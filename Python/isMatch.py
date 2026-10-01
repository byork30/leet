class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ip = 0
        i = 0
        prevLetter = ""
        isMatch = True
        
        while i < len(s) and ip < len(p):
            if p[ip] == '.':
                i += 1
                ip += 1
            elif p[ip] == '*':
                if p[ip-1] == '.':
                    prevLetter = s[i]
                    i += 1
                else:
                    prevLetter = s[i-1]
                while i < len(s) and s[i] == prevLetter:
                    i += 1
            else:
                if not (s[i] == p[ip]):
                    return False
                ip += 1
                i += 1
        return (isMatch and ip == len(p)-1)
                

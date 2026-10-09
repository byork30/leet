class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = [[s[0]]]
        i = 0
        step = 1
        converted = ""
        for i in range((numRows) - 1):
            zigzag.append([])
        i = 1
        for letter in s[1:]:
            if i == 0:
                step = 1
            elif i == len(zigzag) - 1:
                step = -1
            zigzag[i].append(letter)
            i += step
        for j in range(len(zigzag)):
            for k in range(len(zigzag[j])):
                converted += zigzag[j][k]
        return converted

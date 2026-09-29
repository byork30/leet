class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num == 0):
            return "Zero"
        ones = ("", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ")
        teens = ("Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen ")
        tens = ("", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety ")
        powers = ("", "Thousand ", "Million ", "Billion ")
        power = 0
        answer = ""
        while num > 0:
            group = num % 1000
            if group == 0:
                num //= 1000
                power += 1
                continue
            tempStr = ""
            if (group//100 > 0):
                tempStr = ones[group//100] + "Hundred "
            if ((group // 10) % 10 == 1):
                tempStr += teens[group % 10]
            else:
                tempStr += tens[(group//10)%10] + ones[group%10]
            answer = tempStr + powers[power] + answer
            num //= 1000
            power += 1
        return answer.strip()

class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sm = 0
        prev = 0
        convert = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M':1000}
        for symb in s[::-1]:
            num = convert[symb]
            if prev <= num:
                sm += num
            else:
                sm -= num
            prev = num
        return sm
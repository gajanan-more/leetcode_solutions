class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_value={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        sum = 0
        i = 0
        while (i < len(s)):

            if i == len(s)-1:
                sum += roman_value[s[i]]
                print("if",sum)
                break
            elif roman_value[s[i]] < roman_value[s[i+1]]:
                sum = sum + roman_value[s[i+1]] - roman_value[s[i]]
                print("Elif",sum)
                if i + 1 == len(s)-1:
                    break
                i += 2
            else:
                sum += roman_value[s[i]]
                print("else", sum)
                i += 1
        
        return sum
    
    
    
    
    
    
    
    
    
    
    
    
                
        
        
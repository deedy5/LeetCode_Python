class Solution:
    def romanToInt(self, s: str) -> int:
        '''Given a roman numeral, convert it to an integer
        
        '''
    
        dics = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        summ = 0
        t = 1001        
        for x in s:
            i = dics[x]
            if i <= t:
                summ += i
            else:
                summ += (i - t) - t
            t = i            
        return summ

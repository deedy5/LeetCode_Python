class Solution:
    def reverse(self, x: int) -> int:
        '''Given a 32-bit signed integer, reverse digits of an integer'''
        
        fx = f"{x}"
        
        if x >= 0:
            i = int(fx[::-1])            
        else:
            i = int(f"-{fx[:0:-1]}")
            
        if -2147483648 <= i < 2147483648:
            return i
        return 0

class Solution:
    def isValid(self, s: str) -> bool:
    '''Function determine if the input string is valid.
    
    An input string is valid if:    
      1) Open brackets must be closed by the same type of brackets.
      2) Open brackets must be closed in the correct order.
      3) Empty string is also considered valid.
      
    '''
    
        dics = {')':'(', '}':'{', ']':'['}
        cache = []
        for c in s:
            if cache and c in dics and cache[-1] == dics[c]:
                cache.pop()
            else:
                cache.append(c)
        return not cache

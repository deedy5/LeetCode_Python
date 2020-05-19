class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == '':
            return 0
        
        hl = len(haystack)
        nl = len(needle)
        t = 0
        
        while t  <= hl - nl:
            if needle == haystack[t:nl+t]:                
                return t
            else:
                t += 1
                
        return -1
        
'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Return 0 when needle is an empty string.
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

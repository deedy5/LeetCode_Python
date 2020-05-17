class Solution:
    def isPalindrome(self, x: int) -> bool:
    '''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''
    
        return x >= 0 and x == int(f"{x}"[::-1])

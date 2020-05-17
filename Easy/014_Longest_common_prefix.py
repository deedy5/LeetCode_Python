class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    '''Return the longest common prefix string amongst an array of strings'''
    
        return os.path.commonprefix(strs)

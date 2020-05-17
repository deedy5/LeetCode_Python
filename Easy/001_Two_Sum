class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        cache = {}        
        for i,x in enumerate(nums):
            if target - x in cache:
                return[cache[target - x], i]
            cache[x] = i

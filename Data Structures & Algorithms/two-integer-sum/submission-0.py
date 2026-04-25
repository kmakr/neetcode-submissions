class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rec = {}

        for i, num in enumerate(nums):
            if num in rec:
                return [nums.index(rec[num]), i]
            else:
                rec[target - num] = num
        
        


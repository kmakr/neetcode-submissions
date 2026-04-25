class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}

        for num in nums:

            if num in store:
                store[num] += 1
            else:
                store[num] = 1

            if (store[num] > 1):
                return True
        
        return False
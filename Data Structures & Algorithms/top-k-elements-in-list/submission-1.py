class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        rec = {}

        for num in nums:
            rec[num] = 1 + rec.get(num, 0)

        arr = []
        for num, count in rec.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
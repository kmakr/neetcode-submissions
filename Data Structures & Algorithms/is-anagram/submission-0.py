class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        recordOne = {}
        recordTwo = {}

        for c in s:
            if c in recordOne:
                recordOne[c] += 1
            else:
                recordOne[c] = 0


        for c in t:
            if c in recordTwo:
                recordTwo[c] += 1
            else:
                recordTwo[c] = 0
    
        return recordOne == recordTwo


        
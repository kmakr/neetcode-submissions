class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        known_char = set()
        l = 0
        res = 0

        for r in range(len(s)):

            while s[r] in known_char:
                known_char.remove(s[l])
                l += 1
            
            res = max(res, r - l + 1)
            known_char.add(s[r])
        
        return res


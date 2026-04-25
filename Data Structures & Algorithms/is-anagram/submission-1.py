class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_id = [0] * 26
        t_id = [0] * 26

        for i in range(len(s)):
            s_id[ord(s[i]) - ord('a')] += 1
            t_id[ord(t[i]) - ord('a')] += 1

        return s_id == t_id


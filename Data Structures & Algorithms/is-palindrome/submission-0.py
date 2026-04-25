class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        rec = []
        for c in s:
            if (c.isalnum()):
                rec.append(c)


        return rec == rec[::-1]
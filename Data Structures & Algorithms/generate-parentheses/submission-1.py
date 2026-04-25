class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # finish if n == open bracket count == closed bracket count
        # add ( if openCount < n
        # add ) if closeCount < openCount 

        res = []
        rec = []

        def backtrack(openCount, closeCount):

            if openCount == closeCount == n:
                res.append("".join(rec))
                
            if openCount < n:
                rec.append("(")
                backtrack(openCount + 1, closeCount)
                rec.pop()

            if closeCount < openCount:
                rec.append(")")
                backtrack(openCount, closeCount + 1)
                rec.pop()


        backtrack(0, 0)

        return res
        
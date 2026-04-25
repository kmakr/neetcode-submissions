class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(openCount, closeCount, comboString):

            if openCount == closeCount == n:
                res.append(comboString)

            if openCount < n:
                backtrack(openCount + 1, closeCount, comboString + "(")

            if closeCount < openCount:
                backtrack(openCount, closeCount + 1, comboString + ")")

        backtrack(0, 0, "")

        return res
        
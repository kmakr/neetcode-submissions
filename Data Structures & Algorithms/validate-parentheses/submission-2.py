class Solution:
    def isValid(self, s: str) -> bool:

        bracket_pair = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        record_stack = []

        for c in s:
            if c in bracket_pair.values():
                print ("before append" , record_stack)
                record_stack.append(c)
                print ("after append" , record_stack)

            elif c in bracket_pair.keys():

                if record_stack and record_stack[-1] == bracket_pair[c]:
                    print ("before pop", record_stack)
                    record_stack.pop()
                    print ("after pop", record_stack)

                else:
                    return False
        
        return not record_stack
        
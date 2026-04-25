class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []

        
        for tok in tokens:
            print(nums)
            
            if tok == '+':
                nums.append(nums.pop() + nums.pop())
            elif tok == '-':
                y = nums.pop()
                x = nums.pop()
                nums.append(x - y)
            elif tok == '*':

                nums.append(nums.pop() * nums.pop())
            elif tok == '/':
                # y = nums.pop()
                # x = nums.pop()
                # nums.append(x // y)
                a, b = nums.pop(), nums.pop()
                nums.append(int(float(b)/a)) 
            else:
                nums.append(int(tok))
                    
        return nums[0]

                

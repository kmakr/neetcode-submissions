class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        print(prefix)
        postfix = []
        product = 1
        for num in nums[::-1]:
            product *= num
            postfix.append(product)

        print(postfix)
        postfix.reverse()
        
        res = []
        for i in range(len(nums)):
            final = 1
            # only postfix
            if (i == 0):
                final *= postfix[i + 1]
            # only prefix
            elif (i == len(nums) - 1):
                final *= prefix[i - 1]
            # "normal" case
            else:
                final *= (prefix[i - 1] * postfix[i + 1])

            res.append(final)

        return res

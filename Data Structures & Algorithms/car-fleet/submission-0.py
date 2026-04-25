class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []
        #find speed
        for p, s in sorted(pair)[::-1]: # reverse sorted
            timeToTarget = (target - p) / s

            stack.append(timeToTarget)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # latest car is faster than the previous car (less time to target) then join the fleet
                stack.pop()

        return len(stack)

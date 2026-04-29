class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # count backwards and see if any car will join the fleet at the top of the stack
        # returnn the length of the stack
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
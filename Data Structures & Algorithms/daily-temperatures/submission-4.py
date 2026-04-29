class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                t, l = stack.pop()
                res[l] = i - l
            stack.append((temperature, i))
        return res
                

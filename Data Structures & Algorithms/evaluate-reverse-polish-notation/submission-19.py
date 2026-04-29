class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == "+":
                s.append(s.pop() + s.pop())
            elif token == "-":
                op2 = s.pop()
                op1 = s.pop()
                s.append(op1 - op2)
            elif token == "*":
                s.append(s.pop() * s.pop())
            elif token == "/":
                op2 = s.pop()
                op1 = s.pop()
                s.append(int(float(op1)/ op2))
            else:
                s.append(int(token))
        return s[0]
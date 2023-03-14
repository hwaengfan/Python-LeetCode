class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in signs:
                n2, n1 = stack.pop(), stack.pop()
                stack.append(self.compute(n1, n2, token))
            else:
                stack.append(int(token))
        return stack[-1]

    def compute(self, n1, n2, sign):
        if sign == "+":
            return n1 + n2
        elif sign == "-":
            return n1 - n2
        elif sign == "*":
            return n1 * n2
        else:
            return int(n1 / n2)

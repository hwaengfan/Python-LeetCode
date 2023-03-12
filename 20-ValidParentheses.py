class Solution:
    def isValid(self, s: str) -> bool:
        mapChar = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for c in s:
            if stack and mapChar.get(c, "") == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

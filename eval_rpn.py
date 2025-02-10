import Math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-/*"

        stack = []

        for t in tokens:
            if t in operators:
                result = 0
                r = int(stack.pop())
                l = int(stack.pop())

                if t == "+":
                    result = l + r
                elif t == "-":
                    result = l - r
                elif t == "*":
                    result = l * r
                else:
                    result = l / r

                stack.append(result)
            else:
                stack.append(t)

        return stack.pop()

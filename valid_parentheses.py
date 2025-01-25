class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in close_to_open.keys():
                if stack and stack[0] == close_to_open[c]:
                    stack.pop(0)
                else:
                    return False
            else:
                stack.insert(0, c)

        return len(stack) == 0

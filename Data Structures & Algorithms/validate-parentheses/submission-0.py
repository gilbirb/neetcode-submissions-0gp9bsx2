class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            top = None
            if stack:
                top = stack[-1]
            if ((c == ')' and top == '(') or
               (c == '}' and top == '{') or
               (c == ']' and top == '[')):
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
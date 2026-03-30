class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = ["+", "-", "*", "/"]
        for n in tokens:
            if n in oper:
                n1 = stack.pop()
                n2 = stack.pop()
                if n == "+":
                    stack.append(n1 + n2)
                elif n == "-":
                    stack.append(n2 - n1)
                elif n == "*":
                    stack.append(n1 * n2)
                elif n == "/":
                    stack.append(math.trunc(n2 / n1))
            else:
                num = int(n)
                stack.append(num)
            print(6//-132)
        return stack.pop()
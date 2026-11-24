class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op_2 = int(stack.pop())
                op_1 = int(stack.pop())
                if token == "+":
                    stack.append(op_1 + op_2)
                elif token == "-":
                    stack.append(op_1 - op_2)
                elif token == "*":
                    stack.append(op_1 * op_2)
                else:
                    stack.append(int(op_1 / op_2))
            else:
                stack.append(int(token))
        
        return stack[0]
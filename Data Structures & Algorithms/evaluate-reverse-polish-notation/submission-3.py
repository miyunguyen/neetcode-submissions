class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                match token:
                    case "+":
                        stack.append(first + second)
                    case "-":
                        stack.append(first - second)
                    case "*":
                        stack.append(first * second)
                    case "/":
                        stack.append(int(first / second))
        
        return int(stack[0])
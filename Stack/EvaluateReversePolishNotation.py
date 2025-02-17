class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val2 / val1))
        return stack[-1]


obj = Solution()
tokens = ["1", "2", "+", "3", "*", "4", "-"]
tokens1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(obj.evalRPN(tokens1))

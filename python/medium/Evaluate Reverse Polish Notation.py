class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ('+', '-', '*', '/')
        tmp_stack = []
        for operand in tokens:
            if operand not in operators:
                tmp_stack.append(operand)

            else:
                right_value = int(tmp_stack.pop())
                left_value = int(tmp_stack.pop())
                if operand == '+':
                    tmp_stack.append(left_value + right_value)
                elif operand == '-':
                    tmp_stack.append(left_value - right_value)
                elif operand == '*':
                    tmp_stack.append(left_value * right_value)
                elif operand == '/':
                    tmp_stack.append(int(left_value / right_value))

        return tmp_stack.pop()

if __name__ == '__main__':
    ans = Solution()
    testData = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(ans.evalRPN(testData))
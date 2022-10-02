class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        tmp_stack = []

        for operand in tokens:
            if operand == '+':
                tmp_stack.append(tmp_stack.pop() + tmp_stack.pop())

            elif operand == '-':
                r, l = tmp_stack.pop(), tmp_stack.pop()
                tmp_stack.append(l - r)

            elif operand == '*':
                tmp_stack.append(tmp_stack.pop() * tmp_stack.pop())

            elif operand == '/':
                r, l = tmp_stack.pop(), tmp_stack.pop()
                tmp_stack.append(int(l / r))
            else:
                tmp_stack.append(int(operand))

        return tmp_stack[0]

if __name__ == '__main__':
    ans = Solution()
    testData = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(ans.evalRPN(testData))
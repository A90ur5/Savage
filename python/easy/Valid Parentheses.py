class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for c in s:
            if (c == '(') or (c == '[') or (c == '{'):
                myStack.append(c)

            if c == ')':
                if myStack == [] or myStack.pop() != '(':
                    return False

            elif c == ']':
                if myStack == [] or myStack.pop() != '[':
                    return False

            elif c == '}':
                if myStack == [] or myStack.pop() != '{':
                    return False

        if myStack:
            return False

        else:
            return True

def main():
    mySol = Solution
    a = mySol.isValid(mySol, "]")
    print(a)

if __name__ == '__main__':
     main()

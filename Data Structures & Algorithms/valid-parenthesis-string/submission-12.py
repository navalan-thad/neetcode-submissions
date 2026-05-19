class Solution:
    def checkValidString(self, s: str) -> bool:

        wc = []
        stack = []

        for i in range(len(s)):
            if s[i] == '*':
                wc.append(i)
            elif s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif wc:
                    wc.pop()
                else:
                    return False

        while stack and wc:
            if stack[-1] < wc[-1]:
                stack.pop()
                wc.pop()
            else:
                return False

        return True if len(stack) == 0 else False

        


        
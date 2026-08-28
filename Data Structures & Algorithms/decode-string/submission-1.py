class Solution:
    def decodeString(self, s: str) -> str:

        curr = ''
        k = 0
        stack = []

        for char in s:
            if char == '[':
                stack.append(curr)
                stack.append(k)
                curr = ''
                k = 0

            elif char == ']':
                prev_k = stack.pop()
                prev_str = stack.pop()
                curr = prev_str + prev_k*curr

            else:
                if char.isdigit():
                    k = k*10 + int(char)
                else:
                    curr += char

        return curr


        
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        string = ''
        count = 0

        for char in s:
            if char == '[':
                stack.append(string)
                stack.append(count)
                string = ''
                count = 0
            elif char == ']':
                prev_count = stack.pop()
                prev_str = stack.pop()
                string = prev_str + string*prev_count
            else:
                if char.isdigit():
                    count = count*10 + int(char)
                else:
                    string += char

        return string


        
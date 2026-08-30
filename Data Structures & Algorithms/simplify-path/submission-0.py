class Solution:
    def simplifyPath(self, path: str) -> str:

        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            else:
                if len(part) > 0 and part != '.':
                    stack.append(part)

        res = ''
        for file in stack:
            res += '/' + file

        return '/' if not res else res
        
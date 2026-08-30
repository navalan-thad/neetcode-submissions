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

        return '/' + '/'.join(stack)
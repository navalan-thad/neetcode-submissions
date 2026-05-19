class Solution:
    def isValid(self, s: str) -> bool:

        order = []
        pairings = {'}': '{', ')': '(', ']': '['}

        for i in s:
            if i in ['[', '{', '(']:
                order.append(i)
            else:
                print(order)
                if len(order) > 0 and order[-1] == pairings[i]:
                    order.pop()
                else:
                    return False
        return len(order) == 0
        
class Solution:
    def isValid(self, s: str) -> bool:

        order = []
        pairings = {'}': '{', ')': '(', ']': '['}

        # if s[0] in pairings.keys():
        #     return False

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
        
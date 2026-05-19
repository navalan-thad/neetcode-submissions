class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n != 1:
            if n in visited:
                return False
            
            total = 0
            for i in str(n):
                total += int(i) ** 2
            visited.add(n)
            n = total

        return True

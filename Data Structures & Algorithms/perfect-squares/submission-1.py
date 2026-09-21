class Solution:
    def numSquares(self, n: int) -> int:

        from collections import deque
        import math

        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        q = deque([(n, 0)]) # curr remainder, step count
        visited = {n}

        while q:
            rem, steps = q.popleft()

            for s in squares:
                next_rem = rem - s

                if next_rem == 0:
                    return steps + 1
                elif next_rem < 0: 
                    break

                if next_rem not in visited:
                    visited.add(next_rem)
                    q.append((next_rem, steps+1))

        


        
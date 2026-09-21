class Solution:
    def numSquares(self, n: int) -> int:

        from collections import deque

        i = 1
        squares = []
        while i*i <= n:
            squares.append(i*i)
            i += 1

        q = deque([(n, 0)]) # remainder, steps
        visited = {n}

        while q:
            rem, steps = q.popleft()

            for square in squares:
                next_rem = rem - square

                if next_rem == 0:
                    return steps + 1
                elif next_rem < 0:
                    break

                if next_rem not in visited:
                    visited.add(next_rem)
                    q.append((next_rem, steps+1))

            

                




        
        


        
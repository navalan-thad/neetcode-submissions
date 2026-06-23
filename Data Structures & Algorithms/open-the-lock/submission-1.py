from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        frontier = deque(['0000'])
        deadends = set(deadends)
        visited = set()
        moves = 0
        
        while frontier:

            for _ in range(len(frontier)):
                curr = frontier.popleft()

                if curr == target:
                    return moves
                elif curr in deadends or curr in visited:
                    continue

                visited.add(curr)

                for posn in range(4):
                    start = curr[:posn]
                    end = curr[posn+1:]
                    inc = str((int(curr[posn]) + 1) % 10)
                    dec = str((int(curr[posn]) - 1) % 10)                

                    frontier.append(start + inc + end)
                    frontier.append(start + dec + end)

            moves += 1


        return -1




        
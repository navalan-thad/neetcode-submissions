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
                    if curr[posn] == '9':
                        frontier.append(start + '0' + end)
                        frontier.append(start + '8' + end)
                    elif curr[posn] == '0':
                        frontier.append(start + '1' + end)
                        frontier.append(start + '9' + end)
                    else:
                        mid = int(curr[posn])
                        frontier.append(start + str(mid+1) + end)
                        frontier.append(start + str(mid-1) + end)

            moves += 1


        return -1




        
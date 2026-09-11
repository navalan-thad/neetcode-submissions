import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        if max(freq.values()) > (len(s)+1) // 2:
            return ''

        max_heap = [[-v, k] for k, v in freq.items()]
        heapq.heapify(max_heap)

        timeout = None
        result = []

        while max_heap or timeout:
            if timeout and not max_heap: # only char left is on timeout
                return ''

            count, char = heapq.heappop(max_heap)
            result.append(char)
            count += 1 # decrementing negative freq

            if timeout:
                heapq.heappush(max_heap, timeout)
                timeout = None

            if count < 0:
                timeout = [count, char]

        return ''.join(result)
                




        
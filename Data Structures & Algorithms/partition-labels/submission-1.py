class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        res = []
        curr = set()
        count = 0

        for char in s:
            count += 1
            if char not in curr:
                curr.add(char)
            if freq[char] == 1:
                curr.remove(char)
                if not curr:
                    res.append(count)
                    count = 0
            else:
                freq[char] -= 1

        return res
                

        
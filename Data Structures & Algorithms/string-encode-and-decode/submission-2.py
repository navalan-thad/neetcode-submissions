class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 1. read length
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # 2. read string of that length
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 3. move pointer forward
            i = end

        return res
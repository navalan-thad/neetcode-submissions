class Solution:

    def encode(self, strs: List[str]) -> str:

        breaker = '@$#^%'

        code = []
        for s in strs:
            code.append(s)
            code.append(breaker)
        return "".join(code)


    def decode(self, s: str) -> List[str]:

        strList = s.split('@$#^%')
        strList.pop()
        return strList


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []
        ops = ('+', 'C', 'D')

        for i in operations:
            if i not in ops:
                record.append(int(i))
            elif i == '+':
                record.append(record[-1] + record[-2])
            elif i == 'D':
                record.append(record[-1] * 2)
            elif i == 'C':
                record.pop()
            print(record)
        return sum(record)
        